---
layout: article
title: CANARD
description: "40,527 question-rewriting pairs for conversational QA, testing coreference resolution and ellipsis in multi-turn dialog. Built on the QuAC dataset. Licensed CC BY-SA 4.0."
venue: EMNLP 2019
year: 2019
badges: [dataset]
---

# CANARD: Question-in-Context Rewriting

CANARD is a crowdsourced dataset for question rewriting in conversational contexts. It contains **40,527 question-rewriting pairs** designed to evaluate models handling coreference resolution and ellipsis — the two most common reasons conversational questions are hard to answer in isolation.

CANARD is built on top of [QuAC](https://quac.ai), a conversational reading comprehension dataset based on Wikipedia articles.

## Dataset Statistics

| Split | Examples |
|---|---|
| Train | 31,526 |
| Dev | 3,430 |
| Test | 5,571 |
| Reference (dual-annotated) | 100 pairs |

## Data Format

Each JSON entry contains:

| Field | Description |
|---|---|
| `History` | Previous dialog utterances |
| `Question` | Original question from conversation |
| `Rewrite` | Context-independent rewrite |
| `QuAC_dialog_id` | Source dialog identifier |
| `Question_no` | Question number within dialog |

## Resources

- **Paper**: [Can You Unpack That? Learning to Rewrite Questions-in-Context](https://aclanthology.org/D19-1605/) — EMNLP 2019
- **Code & data**: [github.com/aagohary/canard](https://github.com/aagohary/canard)
- **License**: CC BY-SA 4.0

## Citation

> Ahmed Elgohary, Denis Peskov, Jordan Boyd-Graber.
> **Can You Unpack That? Learning to Rewrite Questions-in-Context.**
> *EMNLP 2019.*

## Contact

Ahmed Elgohary — elgohary@cs.umd.edu
