---
layout: article
title: "2026 Competition: Computer Rules"
---

# Computer Rules — QANTA 2026

These rules govern model submissions, evaluation, and leaderboard reporting for the QANTA 2026 computer track.

The computer track builds on the EfficientQA competition framework, adapted for multimodal, pyramidal quizbowl questions.

## Core Task

Systems receive incrementally revealed multimodal clues (text plus images) and must output:

1. A predicted answer string
2. A binary commitment indicator (`commit` or `do_not_commit`)

The commitment indicator is required at each decision point and is used to evaluate both answering quality and calibration quality.

## Track Structure

As in EfficientQA-style evaluation, QANTA 2026 includes restrained and open settings to compare systems under practical constraints.

Current tracks:

- **Restricted Track (6 GB)**: most accurate self-contained system under 6 GB
- **Restricted Track (500 MB)**: most accurate self-contained system under 500 MB
- **Open Track**: highest overall accuracy, regardless of model size

System size is measured from a fully self-contained runtime package. Submissions may not call external APIs at evaluation time.

## Data and Question Format

QANTA 2026 uses multimodal, pyramidal question streams rather than only static text QA examples.

- Questions become easier as clues are revealed
- Image clues can appear alongside text clues
- Systems should decide whether to commit early or wait for additional evidence

## Evaluation Process

Submissions are evaluated in two phases:

1. **Automatic evaluation** produces initial leaderboard rankings.
2. **Human verification** is used for top systems where answer equivalence is ambiguous.

Final rankings are based on the official post-verification results.

## Leaderboard Metrics

The public leaderboard reports:

- **Overall accuracy**
- **Calibrated accuracy**

Calibrated accuracy rewards systems that commit when likely correct and refrain when uncertain. This metric is reported alongside standard accuracy, not as a replacement for it.

## Submission Requirements

Each submission must provide:

- A runnable, self-contained system artifact
- Prediction outputs in the required format
- A binary commitment flag for each prediction point
- Documentation of model size and runtime assumptions

Detailed packaging and file format instructions will be posted with the final submission template.

## Reference

The competition design is adapted from EfficientQA task principles and extended for multimodal, incremental quizbowl play.

> [EfficientQA Task Definition](https://efficientqa.github.io/task_definition.html)

## Contact

Questions about computer rules? Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
