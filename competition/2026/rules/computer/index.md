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
directly: each correct part gives 3.33 points each.

### Combining and Normalizing

To make the scores more comparable between human and computer teams,
we upweight the role of the calibrated questions.  In the human
competition, the bonus is *conditional* on getting the initial
question correct.

There will be the same number of calibrated and uncalibrated
questions, and we will divide by the total number of questions to
create a number between 0 and 1.

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
size of a system is S, then the points V' for the system that had V
raw points is:
$$
V' = V \left(1 - \frac{S}{C} \right)
$$

### Computing the Deflation

We will publish an official plan for computing the deflation (taking
into account base models for prompt-based systems) on May 1, allow
potential submitters to comment until May 15, and we will publish the
final framework May 18.

Feedback on the scoring framework or challenge metric should be sent to [emm-qa-organizers@googlegroups.com](mailto:emm-qa-organizers@googlegroups.com) by June 1, 2026.

### Leaderboard columns

The public leaderboard reports at least:

- **Overall points (automatic)** (answer correctness under the official evaluation protocol)
- **Calibrated accuracy** (rewards committing when correct and refraining when uncertain — reported alongside raw accuracy, not as a replacement)

Final ranks for prizes use the **Overall points (human)** score where
human review resolves ambiguous answer equivalence (see Evaluation
process).  All adjudications will be made public.

Prize amounts and special awards are summarized on the [Prizes](/competition/2026/prizes/) page.

### Unofficial Prizes

While not for prize money, we will also offer recognition for the
system that:
- Best boosted human accuracy (including adjusted by overall accuracy)
- Was most chosen by human teams(including adjusted by overall
accuracy)
- Best system from an academic team
- Best system from undergraduates
- Best system from secondary education 


## Track structure

As in EfficientQA-style evaluation, QANTA 2026 includes restrained and open settings:

- **Middleweight (6 GB):** most accurate self-contained system under 6 GB
- **Lightweight (500 MB):** most accurate self-contained system under 500 MB
- **Heavyweight:** highest performance without the above size caps (but
  implicitly capped based on what our system submission can support)

System size is measured from a **fully self-contained** artifact (code, weights, data packaged for evaluation). Submissions may **not** call external APIs at evaluation time.


## Reference

> [EfficientQA Task Definition](https://efficientqa.github.io/task_definition.html)

## Contact

Questions about computer rules? Email [emm-qa-organizers@googlegroups.com](mailto:emm-qa-organizers@googlegroups.com).
