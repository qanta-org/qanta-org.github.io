#!/usr/bin/env python3
"""Refactor a Protobowl buzz log into normalized question and buzz files."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import sqlite3
import sys
import tempfile
from contextlib import closing
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from tqdm import tqdm
except ImportError:  # pragma: no cover - optional dependency
    tqdm = None


DATE_FORMAT = "%a %b %d %Y %H:%M:%S GMT%z"
DEFAULT_OUTPUT_DIR = Path("research/data/protobowl")
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def canonical_question_payload(record: dict[str, Any]) -> dict[str, Any]:
    question_info = record.get("question_info") or {}
    return {
        "question_info": question_info,
        "question_text": record.get("question_text"),
        "answer": record.get("answer"),
    }


def question_id_for(record: dict[str, Any]) -> str:
    payload = canonical_question_payload(record)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()
    return f"protobowl-{digest}"


def parse_event_time(raw_date: str) -> int:
    cleaned = raw_date
    if " (" in cleaned:
        cleaned = cleaned.split(" (", 1)[0]
    return int(datetime.strptime(cleaned, DATE_FORMAT).timestamp())


def normalize_user(user: dict[str, Any] | None) -> tuple[str, dict[str, Any]]:
    user = user or {}
    user_id = user.get("id")
    user_name = user.get("name")
    user_key = user_id or f"name:{user_name}" or "unknown"
    normalized = {"id": user_id, "name": user_name}
    return user_key, normalized


def shard_for_user_key(user_key: str) -> str:
    digest = hashlib.sha256(user_key.encode("utf-8")).digest()
    return ALPHABET[digest[0] % len(ALPHABET)]


def count_lines(path: Path) -> int:
    total = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            total += chunk.count(b"\n")
    return total


def compute_buzz_metrics(
    time_elapsed: float | int | None,
    time_remaining: float | int | None,
) -> dict[str, float | int | None]:
    result: dict[str, float | int | None] = {
        "buzz_position_ratio_time": None,
    }

    if time_elapsed is not None and time_remaining is not None:
        total_window = 0.5 * (float(time_elapsed) + float(time_remaining))
        if total_window > 0:
            result["buzz_position_ratio_time"] = round(float(time_elapsed) / total_window, 6)

    return result


class ProgressBar:
    def __init__(self, total: int | None) -> None:
        self.total = total
        self.count = 0
        self._bar = None
        if tqdm is not None:
            self._bar = tqdm(total=total, unit="lines", smoothing=0.05)

    def update(self, amount: int = 1) -> None:
        self.count += amount
        if self._bar is not None:
            self._bar.update(amount)

    def set_postfix(self, buzzes: int, questions: int) -> None:
        if self._bar is not None:
            self._bar.set_postfix(
                {
                    "buzzes": f"{buzzes:,}",
                    "questions": f"{questions:,}",
                },
                refresh=False,
            )

    def close(self) -> None:
        if self._bar is not None:
            self._bar.close()
            return
        if self.total is None:
            print(f"Processed {self.count:,} lines", file=sys.stderr)
            return
        percent = 100.0 if self.total == 0 else 100.0 * self.count / self.total
        print(
            f"Processed {self.count:,}/{self.total:,} lines ({percent:.1f}%)",
            file=sys.stderr,
        )


def ensure_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode = WAL;
        PRAGMA synchronous = NORMAL;

        CREATE TABLE IF NOT EXISTS questions (
            question_id TEXT PRIMARY KEY,
            payload_json TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS buzzes (
            sequence_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_key TEXT NOT NULL,
            event_time INTEGER NOT NULL,
            payload_json TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS user_counts (
            user_key TEXT PRIMARY KEY,
            buzz_count INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS users (
            user_key TEXT PRIMARY KEY,
            payload_json TEXT NOT NULL
        );
        """
    )


def ingest_file(
    input_path: Path,
    connection: sqlite3.Connection,
    line_total: int | None,
    progress_every: int,
    limit: int | None,
) -> tuple[int, int]:
    total_records = 0
    distinct_questions = 0
    insert_question = (
        "INSERT OR IGNORE INTO questions (question_id, payload_json) VALUES (?, ?)"
    )
    insert_buzz = (
        "INSERT INTO buzzes (user_key, event_time, payload_json) VALUES (?, ?, ?)"
    )
    upsert_user_count = """
        INSERT INTO user_counts (user_key, buzz_count)
        VALUES (?, 1)
        ON CONFLICT(user_key) DO UPDATE SET buzz_count = buzz_count + 1
    """
    insert_user = "INSERT OR IGNORE INTO users (user_key, payload_json) VALUES (?, ?)"
    progress = ProgressBar(total=line_total)

    with input_path.open("r", encoding="utf-8") as handle, closing(connection.cursor()) as cursor:
        for line in handle:
            progress.update(1)
            if not line.strip():
                continue

            payload = json.loads(line)
            if payload.get("action") != "buzz":
                continue

            total_records += 1
            obj = payload.get("object") or {}
            qid = question_id_for(obj)
            question_payload = canonical_question_payload(obj)

            cursor.execute(
                insert_question,
                (qid, json.dumps({"question_id": qid, **question_payload}, sort_keys=True)),
            )
            if cursor.rowcount:
                distinct_questions += 1

            user_key, _user_payload = normalize_user(obj.get("user"))
            cursor.execute(
                insert_user,
                (
                    user_key,
                    json.dumps({"user_key": user_key}, sort_keys=True),
                ),
            )

            event_time = parse_event_time(payload["date"])
            buzz_payload = {
                "question_id": qid,
                "date": payload["date"],
                "room": obj.get("room"),
                "playback_rate": obj.get("playback_rate"),
                "guess": obj.get("guess"),
                "ruling": obj.get("ruling"),
                "time_elapsed": obj.get("time_elapsed"),
                "time_remaining": obj.get("time_remaining"),
                **compute_buzz_metrics(
                    obj.get("time_elapsed"),
                    obj.get("time_remaining"),
                ),
            }

            cursor.execute(
                insert_buzz,
                (
                    user_key,
                    event_time,
                    json.dumps(buzz_payload, sort_keys=True),
                ),
            )
            cursor.execute(upsert_user_count, (user_key,))

            if total_records % progress_every == 0:
                connection.commit()
                progress.set_postfix(total_records, distinct_questions)

            if limit is not None and total_records >= limit:
                break

        connection.commit()

    progress.close()
    return total_records, distinct_questions


def write_questions(connection: sqlite3.Connection, output_path: Path) -> int:
    questions: list[dict[str, Any]] = []
    with closing(connection.cursor()) as cursor:
        for (payload_json,) in cursor.execute(
            "SELECT payload_json FROM questions ORDER BY question_id"
        ):
            questions.append(json.loads(payload_json))

    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(questions, handle, indent=2, sort_keys=True)
        handle.write("\n")

    return len(questions)


def write_buzz_shards(
    connection: sqlite3.Connection,
    output_dir: Path,
    minimum_user_buzzes: int,
    sample_path: Path,
    sample_users: int,
) -> tuple[int, list[float], int]:
    query = """
        SELECT b.user_key, u.payload_json, c.buzz_count, b.payload_json
        FROM buzzes AS b
        JOIN user_counts AS c
            ON c.user_key = b.user_key
        JOIN users AS u
            ON u.user_key = b.user_key
        WHERE c.buzz_count >= ?
        ORDER BY b.user_key, b.event_time, b.sequence_id
    """
    shard_handles: dict[str, Any] = {}
    shard_first_record: dict[str, bool] = {}
    current_user_key: str | None = None
    current_group: dict[str, Any] | None = None
    current_shard: str | None = None
    total_buzzes = 0
    total_users = 0
    time_ratios: list[float] = []
    sample_groups: list[dict[str, Any]] = []

    def get_handle(shard: str) -> Any:
        handle = shard_handles.get(shard)
        if handle is None:
            shard_path = output_dir / f"protobowl-buzzes-by-user-{shard}.json.gz"
            handle = gzip.open(shard_path, "wt", encoding="utf-8")
            handle.write("[\n")
            shard_handles[shard] = handle
            shard_first_record[shard] = True
        return handle

    def flush_group(group: dict[str, Any] | None, shard: str | None) -> None:
        nonlocal total_users
        if group is None or shard is None:
            return

        handle = get_handle(shard)
        if not shard_first_record[shard]:
            handle.write(",\n")
        handle.write(json.dumps(group, indent=2, sort_keys=True))
        shard_first_record[shard] = False
        total_users += 1

        if len(sample_groups) < sample_users:
            sample_groups.append(group)

    with closing(connection.cursor()) as cursor:
        for user_key, _user_payload_json, buzz_count, payload_json in cursor.execute(
            query, (minimum_user_buzzes,)
        ):
            if buzz_count < 25:
                continue
            buzz_payload = json.loads(payload_json)

            if user_key != current_user_key:
                flush_group(current_group, current_shard)
                current_user_key = user_key
                current_shard = shard_for_user_key(user_key)
                current_group = {
                    "user": user_key,
                    "user_buzz_count": buzz_count,
                    "user_buzzes": [],
                }

            assert current_group is not None
            current_group["user_buzzes"].append(buzz_payload)
            total_buzzes += 1

            if buzz_payload.get("buzz_position_ratio_time") is not None:
                time_ratios.append(float(buzz_payload["buzz_position_ratio_time"]))

    flush_group(current_group, current_shard)

    for shard in ALPHABET:
        handle = shard_handles.get(shard)
        shard_path = output_dir / f"protobowl-buzzes-by-user-{shard}.json.gz"
        if handle is None:
            with gzip.open(shard_path, "wt", encoding="utf-8") as empty_handle:
                empty_handle.write("[\n]\n")
        else:
            handle.write("\n]\n")
            handle.close()

    with sample_path.open("w", encoding="utf-8") as handle:
        json.dump(sample_groups, handle, indent=2, sort_keys=True)
        handle.write("\n")

    return total_buzzes, time_ratios, total_users


def build_histogram(values: list[float], bins: int, upper_bound: float) -> list[dict[str, float | int]]:
    if not values:
        return []

    width = upper_bound / bins
    counts = [0 for _ in range(bins)]

    for value in values:
        clipped = min(max(value, 0.0), upper_bound)
        index = min(int(clipped / width), bins - 1)
        counts[index] += 1

    histogram = []
    for index, count in enumerate(counts):
        histogram.append(
            {
                "start": round(index * width, 6),
                "end": round((index + 1) * width, 6),
                "count": count,
            }
        )
    return histogram


def write_histogram_svg(
    histogram_path: Path,
    time_ratios: list[float],
    bins: int = 25,
    upper_bound: float = 2.5,
) -> None:
    time_hist = build_histogram(time_ratios, bins, upper_bound)
    all_counts = [item["count"] for item in time_hist]
    max_count = max(all_counts) if all_counts else 1

    width = 1000
    height = 340
    margin_left = 80
    margin_right = 30
    chart_width = width - margin_left - margin_right
    panel_height = 210
    top_margin = 80

    if not time_hist:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  <text x="{margin_left}" y="30" font-size="24" font-family="sans-serif">Protobowl Buzz Ratio Histogram</text>
  <text x="{margin_left}" y="70" font-size="18" font-family="sans-serif">No data</text>
</svg>
"""
        histogram_path.write_text(svg, encoding="utf-8")
        return

    bin_width = chart_width / len(time_hist)
    elements = [
        f'<text x="{margin_left}" y="30" font-size="24" font-family="sans-serif">Protobowl Buzz Ratio Histogram</text>',
        f'<text x="{margin_left}" y="50" font-size="13" fill="#555" font-family="sans-serif">buzz_position_ratio_time = elapsed / (0.5 * (elapsed + remaining)). X-axis clipped to 2.5.</text>',
        f'<line x1="{margin_left}" y1="{top_margin + panel_height}" x2="{margin_left + chart_width}" y2="{top_margin + panel_height}" stroke="#333" stroke-width="1"/>',
        f'<line x1="{margin_left}" y1="{top_margin}" x2="{margin_left}" y2="{top_margin + panel_height}" stroke="#333" stroke-width="1"/>',
    ]

    for tick in range(5):
        y = top_margin + panel_height - (panel_height * tick / 4.0)
        value = round(max_count * tick / 4.0)
        elements.append(
            f'<line x1="{margin_left - 6}" y1="{y:.1f}" x2="{margin_left}" y2="{y:.1f}" stroke="#333" stroke-width="1"/>'
        )
        elements.append(
            f'<text x="{margin_left - 12}" y="{y + 5:.1f}" font-size="11" text-anchor="end" font-family="sans-serif">{value}</text>'
        )

    for index, bucket in enumerate(time_hist):
        bar_height = 0 if max_count == 0 else panel_height * (int(bucket["count"]) / max_count)
        x = margin_left + index * bin_width + 2
        y = top_margin + panel_height - bar_height
        elements.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(bin_width - 4, 1):.1f}" height="{bar_height:.1f}" fill="#4C78A8" opacity="0.8"/>'
        )

    label_step = max(1, len(time_hist) // 5)
    for index, bucket in enumerate(time_hist):
        if index % label_step != 0 and index != len(time_hist) - 1:
            continue
        x = margin_left + index * bin_width
        elements.append(
            f'<text x="{x:.1f}" y="{top_margin + panel_height + 20}" font-size="11" font-family="sans-serif">{bucket["start"]:.2f}</text>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  {''.join(elements)}
</svg>
"""
    histogram_path.write_text(svg, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Normalize a Protobowl buzz log into question and sharded buzz JSON outputs."
    )
    parser.add_argument("input_path", type=Path, help="Path to the Protobowl NDJSON log file")
    parser.add_argument(
        "--questions",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / "protobowl-questions.json",
        help="Output path for normalized question records",
    )
    parser.add_argument(
        "--buzzes",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / "buzzes",
        help="Output directory for gzipped buzz shards grouped by user",
    )
    parser.add_argument(
        "--histogram",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / "protobowl-buzz-ratios.svg",
        help="Output path for the buzz-ratio histogram SVG",
    )
    parser.add_argument(
        "--sample",
        type=Path,
        default=DEFAULT_OUTPUT_DIR / "protobowl-buzzes-sample.json",
        help="Output path for a small uncompressed sample of grouped buzz records",
    )
    parser.add_argument(
        "--sample-users",
        type=int,
        default=5,
        help="Number of grouped user records to include in the sample file",
    )
    parser.add_argument(
        "--minimum-user-buzzes",
        type=int,
        default=10,
        help="Only include users with at least this many buzzes in the buzz output",
    )
    parser.add_argument(
        "--progress-every",
        type=int,
        default=100000,
        help="Refresh the progress details after this many buzz records",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only ingest this many buzz records, useful for sanity checks",
    )
    parser.add_argument(
        "--temp-dir",
        type=Path,
        default=None,
        help="Directory to store the temporary SQLite database",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.minimum_user_buzzes < 1:
        raise SystemExit("--minimum-user-buzzes must be at least 1")
    if args.progress_every < 1:
        raise SystemExit("--progress-every must be at least 1")
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.sample_users < 1:
        raise SystemExit("--sample-users must be at least 1")

    args.questions.parent.mkdir(parents=True, exist_ok=True)
    args.buzzes.mkdir(parents=True, exist_ok=True)
    args.histogram.parent.mkdir(parents=True, exist_ok=True)
    args.sample.parent.mkdir(parents=True, exist_ok=True)

    line_total = count_lines(args.input_path)
    if args.limit is not None:
        line_total = min(line_total, args.limit)

    temp_dir = str(args.temp_dir) if args.temp_dir else None
    fd, sqlite_path = tempfile.mkstemp(
        prefix="protobowl-refactor-",
        suffix=".sqlite3",
        dir=temp_dir,
    )
    os.close(fd)

    try:
        with sqlite3.connect(sqlite_path) as connection:
            ensure_schema(connection)
            total_records, distinct_questions = ingest_file(
                args.input_path,
                connection,
                line_total,
                args.progress_every,
                args.limit,
            )
            question_count = write_questions(connection, args.questions)
            buzz_count, time_ratios, user_count = write_buzz_shards(
                connection,
                args.buzzes,
                args.minimum_user_buzzes,
                args.sample,
                args.sample_users,
            )

        write_histogram_svg(args.histogram, time_ratios)

        print(
            (
                f"Wrote {question_count:,} questions to {args.questions}, "
                f"{buzz_count:,} buzzes across {user_count:,} users into shards under {args.buzzes}, "
                f"sample to {args.sample}, and histogram to {args.histogram} "
                f"from {total_records:,} input buzzes with {distinct_questions:,} distinct questions."
            ),
            file=sys.stderr,
        )
        return 0
    finally:
        try:
            os.remove(sqlite_path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
