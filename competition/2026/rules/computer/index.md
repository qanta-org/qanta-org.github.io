---
layout: article
title: "2026 Competition: Computer Rules"
---

# Computer Rules — QANTA 2026

These rules govern **submitted systems**: inputs and outputs, tracks, evaluation, and **how scores are computed** for the leaderboard and prizes. Live tossup–bonus flow for humans is in the [rules overview](/competition/2026/rules/) and [Human Rules](/competition/2026/rules/human/).

The computer track builds on ideas from the [EfficientQA task](https://efficientqa.github.io/task_definition.html), adapted for **multimodal, pyramidal** quiz bowl questions.

## Core task

Systems receive incrementally revealed multimodal clues (text and images) and must output:

1. A predicted **answer string**
2. A binary **commitment** indicator (`commit` or `do_not_commit`) at
each decision point

Optionally, the models can also output a real-valued confidence, which
will not be used for scoring but will help us with the analysis.

Commitment is how we measure both **whether the system answers** and **whether it knows when to abstain** until more clues appear.

### Calibrated per-question points

For each question, a system that commits to a correct answer earns a
base of **10** points plus a term for **how early** it committed on
the pyramidal question (reported by **quartile** of the reveal
position: earlier correct commits score higher). In other words, first
quartile systems get three points, second quartile get two, third
quartile get one.

An additional two point **power** applies for committing correctly at the
**first** possible decision point (buzzing “at the very top” of the
pyramid).

### Uncalibrated per-question points

Other questions are not calibrated.  These "bonus" questions are cases
where humans will confer on the final answer.  These are scored more
directly: each correct part gives three points each.

### Commentary

To make the scores more comparable between human and computer teams,
we upweight the role of the calibrated questions.  In the human
competition, the bonus is *conditional* on getting the initial
question correct.

## Scoring and ranking of systems

Leaderboard ranking uses a **size-adjusted** score built from
per-question accuracy within a class (e.g., we give out a prize for
each size class such as 500MB, but you can still win that class if you
have a smaller model that is worse at accuracy if it's much smaller
than your competitors).

### Size deflation

Raw totals are **deflated by system size**: accumulated points are
divided by a size term derived from the self-contained submission (so
smaller, efficient systems are not dominated by larger ones on the
same raw accuracy).

If the maximum size of a system in a class is C, and the registered
size of a system is S, then the score for the system is:

### Leaderboard columns

The public leaderboard reports at least:

- **Overall accuracy** (answer correctness under the official evaluation protocol)
- **Calibrated accuracy** (rewards committing when correct and refraining when uncertain — reported alongside raw accuracy, not as a replacement)

Final ranks for prizes use the **official post-verification** score where human review resolves ambiguous answer equivalence (see Evaluation process).

Prize amounts and special awards are summarized on the [Prizes](/competition/2026/prizes/) page.

## Track structure

As in EfficientQA-style evaluation, QANTA 2026 includes restrained and open settings:

- **Restricted (6 GB):** most accurate self-contained system under 6 GB
- **Restricted (500 MB):** most accurate self-contained system under 500 MB
- **Open:** highest performance without the above size caps (but
  implicitly capped based on what our system submission can support)

System size is measured from a **fully self-contained** artifact (code, weights, data packaged for evaluation). Submissions may **not** call external APIs at evaluation time.

## Data and question format

- Questions are **pyramidal**: clues arrive in order; difficulty decreases as more is revealed.
- **Image** clues may appear with text.
- Systems choose **when** to output `commit` versus `do_not_commit` as clues stream in.

## Evaluation process

1. **Automatic evaluation** produces initial rankings and metrics.
2. **Human verification** is applied where needed (e.g., top systems, or when reference answers are incomplete).

Final standings use verified results.

## Submission requirements

Each submission must include:

- A runnable, self-contained system artifact
- Predictions in the required format
- A commitment flag at each required decision point
- Documentation of model size and runtime assumptions

Detailed packaging and file formats will ship with the final submission template.

## Reference

> [EfficientQA Task Definition](https://efficientqa.github.io/task_definition.html)

## Contact

Questions about computer rules? Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
