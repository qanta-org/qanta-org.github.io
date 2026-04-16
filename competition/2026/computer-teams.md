---
layout: article
title: "2026 Competition: Computer Teams"
permalink: /competition/2026/computer-teams/
---

# Computer Teams — QANTA 2026

QANTA 2026 is the first quiz bowl competition to include **multimodal questions** — text clues combined with images. AI systems must handle both modalities to compete.

> Join the community on [Discord](https://discord.gg/pfdfaygr).

For the current rules, see the [rules overview](/competition/2026/rules/) and the [computer rules](/competition/2026/rules/computer/).

## What Your System Must Do

Participating systems receive questions incrementally (word by word for text clues, image at display time for visual clues) and may buzz in at any point to answer. A successful system must:

- **Process text clues** in the pyramid-style, real-time buzz format used in prior QANTA competitions
- **Process image clues** when they appear mid-question — interpreting photographs, artworks, diagrams, maps, or scientific figures
- **Integrate both modalities** to update its answer hypothesis and confidence as new clues arrive
- **Express calibrated confidence** — the scoring rewards systems that know when they don't know

## Scoring

Scoring details to be announced. The format will follow the QANTA 2025 precedent with extensions for multimodal calibration evaluation:

- Accuracy of final answer
- Early buzz bonus (correct answers with fewer clues seen score higher)
- Calibration score (confidence should correlate with accuracy)
- Multimodal bonus track: performance on image-containing questions specifically

The full scoring details are described on the [computer rules](/competition/2026/rules/computer/) page.

## Prizes

Computer teams are eligible for class-based awards and additional recognition for standout systems. See the [prizes and awards](/competition/2026/prizes/) page for the full breakdown.

## Developing your model

### Hosted Agent Creator (recommended to start)

1. Open the competition **Quizbowl Agent Creator** Space: [qanta-challenge/quizbowl-submission](https://huggingface.co/spaces/qanta-challenge/quizbowl-submission).
2. Use the **Tossup Agents** and **Bonus Round Agents** tabs to design a **workflow**: choose provider models, system prompts, optional multi-step pipelines, and buzzer settings. Questions may include **images** as well as text; the interface attaches images automatically when the dataset provides them.
3. Run your agent on sample questions, inspect visualizations, and use **Evaluate** for a fuller check before you submit.
4. For more details on the interface, visit last year's [tossup-guide](https://github.com/qanta-org/QANTA25/blob/main/tossup-agent-guide.md) and [bonus-guide](https://github.com/qanta-org/QANTA25/blob/main/bonus-agent-guide.md).
5. You can **Export Pipeline** to save a YAML snapshot of your configuration for your records or for editing offline.

### Hugging Face pipeline loading

Hub submissions must be **public** and **non-gated**, and loadable as:

```python
from transformers import pipeline

tossup = pipeline(task="quizbowl-tossup", model="<your-username/your-repo-name>")
bonus = pipeline(task="quizbowl-bonus", model="<your-username/your-repo-name>")
```

Custom task registration follows Hugging Face’s [custom pipeline](https://huggingface.co/docs/transformers/en/add_new_pipeline) conventions; starter patterns are linked from the **Hugging Face Pipelines** tab in the submission Space.

## Technical Requirements

Evaluation calls your system with **structured inputs** and expects **structured outputs**. The following table showcases our system requirements.

### Tossups

| Role | Workflow (Tossup Agents tab) | Hub `pipeline(task="quizbowl-tossup", …)` |
|------|------------------------------|-------------------------------------------|
| **Inputs** | `question_text` (string): text revealed so far.<br>`question_images` (optional): list of images for the current prefix; may be empty on text-only questions. | `question_text` (string): text revealed so far.<br>`images` (optional): list of image paths or PIL images when the question includes figures. |
| **Outputs** | **`answer`** (string), **`confidence`** (float, typically 0.0–1.0), wired from your last step. **Buzzing** is not an LLM output field: the **buzzer settings** (e.g. confidence threshold) in the UI decide when a buzz is registered from the confidence trajectory. | **`answer`** (string), **`confidence`** (float, 0.0–1.0), **`buzz`** (bool): whether the model chooses to buzz at this step. |

Intermediate pipeline steps may use additional variables, but the **submitted tossup workflow** must still terminate with **`answer`** and **`confidence`** as the competition-facing outputs.

### Bonuses

Each **part** is evaluated with the leadin plus that part’s text (and any images). Your model is invoked **once per part**.

| Role | Workflow (Bonus Round Agents tab) | Hub `pipeline(task="quizbowl-bonus", …)` |
|------|-----------------------------------|------------------------------------------|
| **Inputs** | `leadin` (string), `part` (string).<br>`leadin_images`, `part_images` (optional lists): images tied to the leadin and to the current part; may be empty. | `leadin` (string), `part` (string).<br>`images` (optional): list of image paths or PIL images for the leadin and part when figures are present. |
| **Outputs** | **`answer`** (string), **`confidence`** (float, 0.0–1.0), **`explanation`** (string): short rationale for the part. | Same three keys: **`answer`**, **`confidence`**, **`explanation`**. |

## Submitting your model

First, register at [qanta-challenge/register](https://huggingface.co/spaces/qanta-challenge/register).

Then, sign in with **Hugging Face** in the submission Space, and use one of the supported submission paths:

### 1. Prompting / workflow interface (default)

On the **Tossup Agents** or **Bonus Round Agents** tab:

1. Complete your workflow so final outputs match **API and technical requirements** above (tossups: **answer**, **confidence**; bonuses: also **explanation**).
2. Enter a **Model name** and short **Description**.
3. Click **Submit** to register your workflow for official evaluation.

### 2. Hugging Face `pipeline` model

Use the **Hugging Face Pipelines** tab to submit a **public, non-gated** model on the Hub that loads with `transformers.pipeline`, following the tables in **API and technical requirements** above (including optional multimodal `images` when your pipeline supports them).

### Docker image submission — *coming soon*

Some teams will want to submit a **Docker image** that runs their own inference stack end-to-end, instead of using the prompting workflow UI or a Hub `pipeline` model. **That option is not available yet.** We plan to support **container-based submissions** in a future update; until then, use the **workflow / prompting** path or the **Hugging Face Pipelines** path above.

For future announcements stay on the mailing list: [emm-qa-organizers@googlegroups.com](mailto:emm-qa-organizers@googlegroups.com)

## Contact

- Email: [emm-qa-organizers@googlegroups.com](mailto:emm-qa-organizers@googlegroups.com)
- Discord: [discord.gg/pfdfaygr](https://discord.gg/pfdfaygr)
