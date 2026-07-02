import argparse
import getpass
import json
import re
from pathlib import Path

import openreview

DEFAULT_USERNAME = "ikuya@ousia.jp"
DEFAULT_VENUE_ID = "ICML.cc/2026/Workshop/EMM-QA"
DEFAULT_OUT_DIR = "accepted_latest_pdfs"


def val(content, *keys, default=""):
    for key in keys:
        if key in content:
            x = content[key]
            return x.get("value", x) if isinstance(x, dict) else x
    return default


def safe_name(s, max_len=150):
    s = re.sub(r'[\\/:\*\?"<>\|\n\r\t]+', "_", str(s).strip())
    s = re.sub(r"\s+", "_", s).strip("._")
    return s[:max_len] or "untitled"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--username", default=DEFAULT_USERNAME)
    ap.add_argument("--venue-id", default=DEFAULT_VENUE_ID)
    ap.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    args = ap.parse_args()

    password = getpass.getpass(f"OpenReview password for {args.username}: ")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net",
        username=args.username,
        password=password,
    )

    notes = client.get_all_notes(content={"venueid": args.venue_id})
    notes = sorted(notes, key=lambda n: n.number or 10**9)

    print(f"venue: {args.venue_id}")
    print(f"accepted papers: {len(notes)}")
    print(f"output: {out_dir}\n")

    rows = []

    for note in notes:
        sid = f"S{int(note.number):04d}"
        title = val(note.content, "title")

        pdf_filename = f"{sid}_{safe_name(title)}.pdf"
        pdf_path = out_dir / pdf_filename

        pdf_bytes = client.get_attachment(id=note.id, field_name="pdf")
        pdf_path.write_bytes(pdf_bytes)

        print(f"saved: {pdf_path}")

        rows.append({
            "submission_number": note.number,
            "submission_id": sid,
            "title": title,
            "archival_options": val(note.content, "archival_options"),
            "pdf_filename": pdf_filename,
        })

    metadata_path = out_dir / "metadata.jsonl"
    with metadata_path.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"\nsaved metadata: {metadata_path}")


if __name__ == "__main__":
    main()
