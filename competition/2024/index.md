---
layout: article
title: 2024 Competition
---

# 2024 Human vs. Computer Competition

QANTA 2024 ran at three sites: **MIT**, **Berkeley**, and **online**.

For more details, see our ACL 2025 paper [GRACE](https://aclanthology.org/2025.acl-long.962.pdf) and the [code and dataset repository](https://github.com/Pinafore/advcalibration).

---

## MIT Mirror Results

Final team standings (by total wins):

1. **Michael's Team** — $150
2. **Joy's Team** — $100
3. **Andrew's Team** — $50

### Main round stats

| Team | Total Wins | Games Played |
|---|---:|---:|
| Michael | 5.5 | 7 |
| Joy | 4.5 | 7 |
| Andrew | 4 | 7 |
| Kevin | 1 | 7 |
| Ishaan | 0 | 7 |
| GPT4o | 4 | 4 |
| GPT4 | 3 | 6 |
| Mistral | 3 | 5 |

### Finals score

| Team | Score |
|---|---:|
| Michael | 105 |
| Joy | 75 |

---

## Berkeley Mirror Results

- Due to unforeseen circumstances, the original two teams were combined into one for four rounds of the tournament and named Berkeley Combined.
- Every player who participated in the competition was awarded $50.

### Main round stats

| Team | Total Wins | Games Played |
|---|---:|---:|
| Berkeley Combined | 4 | 4 |
| Berkeley A | 0 | 4 |
| Berkeley B | 3 | 4 |
| GPT4o | 2 | 3 |
| GPT4 | 2 | 3 |
| Mistral | 0 | 3 |

---

## Online Mirror Results

Final team standings (by total wins):

1. **Goon Squad** — $150
2. **Jhajhria et UCLA** — $100
3. **Mira Loma** — $50

### Main round stats

| Team | Total Wins | Human-Human Wins | Games Played |
|---|---:|---:|---:|
| Goon Squad | 9 | 6 | 10 |
| Jhajhria et UCLA | 7 | 4 | 10 |
| Mira Loma | 6 | 4 | 10 |
| WHISK | 6 | 3 | 10 |
| UBC | 5 | 2 | 10 |
| Gamers Power Tossups | 4 | 3 | 10 |
| CWRU | 4 | 3 | 10 |
| Spencer Manning | 3 | 3 | 10 |
| GPT4o | 8 | — | 11 |
| GPT4 | 4 | — | 9 |
| Mistral | 0 | — | 12 |

For model teams, only games played against human teams are counted.

---

## QANTA 2024 dataset

All competition questions with annotated buzzpoints are in the [released dataset](https://github.com/Pinafore/advcalibration/blob/main/%5Bpublic%5DALL_final_buzzpoints_enc.zip) (ZIP, password: `buzzbuzz`).

### Fields

| Field | Meaning |
|-------|---------|
| `tossup_index` | Tossup id |
| `category` | Subject category |
| `question` | Full tossup text |
| `answer` | Answerline |
| `question_buzzpoints` | Same text with buzz markers inserted (e.g. `[H9, +]` = human team 9, correct; `[M1, -]` = model team 1, incorrect) |
| `position` | Map from whitespace token index (0-based) to that marker. Example: `58` → buzz after the 58th token |

### Example

```json
{
  "tossup_index": "exh-4",
  "category": "Painting/Sculpture",
  "question": "A painting of Cupid hangs in the background of a painting by this artist in which a man leans over a seated woman holding sheet music. In another painting by this artist, the central figure clutches her breast as she looks up at a glass ball suspended from the ceiling by a blue ribbon. Many paintings by this artist depict the same corner of a studio, often decorated with a large map, with a window on the left wall. In one portrait, this artist used lead-tin yellow for the dress of a woman wearing a blue apron and pouring a jug. For 10 points, name this Dutch Golden Age painter of The Milkmaid and Girl with a Pearl Earring.",
  "answer": "Johannes Vermeer",
  "question_buzzpoints": "... Many paintings by this artist [H9, +] depict the same corner of a studio ...",
  "position": [
    {
      "58": "[H9, +]"
    }
  ]
}
```

Note: `question_buzzpoints` is shortened for display here.

---

## Contact

If there are any questions, please email [qanta@googlegroups.com](mailto:qanta@googlegroups.com).
