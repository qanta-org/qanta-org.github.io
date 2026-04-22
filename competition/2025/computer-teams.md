---
layout: article
title: 2025 Competition — Computer Teams
---

## 🤖🛠️ Build an AI Teammate

Build an AI system that teams up with a human to answer trivia questions together. We're testing whether AI systems can know what they don't know — and whether their explanations actually help human players.

Participants can submit systems via a **prompt-based interface** or a **custom Hugging Face model pipeline**.

---

## 🧩 Competition Tasks

### Tossups

Your system continuously analyzes incoming question text, updates its predictions, and decides when to buzz in alongside its human teammate.

- ✅ Correct early buzzes earn points
- ❌ Incorrect buzzes incur penalties

### Bonuses

After winning a tossup, your team answers multi-part bonus questions. Your system should provide:

- An **answer**
- A **confidence score**
- An **explanation** to help your human captain make the final call

See the [bonus scoring mechanism](https://docs.google.com/document/d/1AvCGTBB43SV3iR_q80Y-CEzkZZoQSHD97m90Dg1u1OA/edit?usp=sharing) for full details.

---

## 📊 Evaluation

Systems are scored on **calibration** and **accuracy**. The leaderboard tracks tossup buzzing effectiveness and bonus contribution to human team performance. Calibration is measured via [CALSCORE](https://arxiv.org/abs/2502.19684).

> Final rankings derive from **live human–AI match results**, not leaderboard scores alone.

| Criterion | Description |
|---|---|
| 🎯 **Accuracy** | Correctness on adversarial questions |
| 📐 **Calibration** | Confidence–accuracy correlation |
| 🏟️ **Live performance** | Results from the in-person and online tournaments |

---

## 🏅 Prizes

| Place | Prize |
|---|---|
| 🥇 1st | $200 |
| 🥈 2nd | $150 |
| 🥉 3rd | $100 |
| 4th | $50 |

---

## 🚀 Getting Started

1. [Register on Hugging Face](https://huggingface.co/spaces/qanta-challenge/register)
2. Try the [submission interface](https://huggingface.co/spaces/qanta-challenge/quizbowl-submission)
3. Check the [leaderboard](https://huggingface.co/spaces/qanta-challenge/leaderboard)
4. See the [starter kit](https://github.com/qanta-challenge/qanta25-starter) and [full repo](https://github.com/qanta-challenge/QANTA25) on GitHub

## 🚀 Submission Methods

### Option 1 — Prompt-Based Interface

A browser-based interface supporting models from **OpenAI**, **Cohere**, and **Anthropic**. No custom code required.

### Option 2 — Custom Pipeline

Submit a Hugging Face model pipeline following the provided API specification. See the [starter kit](https://github.com/qanta-challenge/qanta25-starter) and [QANTA25 repo](https://github.com/qanta-challenge/QANTA25) for tutorials and technical specs.

---

## 📅 Key Deadlines

| | Date |
| --- | --- |
| 📊 Leaderboard updates (new questions) | May 23, May 30, June 7 |
| 🏟️ In-Person Tournament submission | June 7, 2025 |
| 🌐 Online Tournament submission (final) | June 14, 2025 |

---

## Contact

Questions? Join the [Discord server](https://discord.gg/E8Z6asZPRt), [open a GitHub issue](https://github.com/qanta-challenge/QANTA25/issues/new), or email [qanta@googlegroups.com](mailto:qanta@googlegroups.com).
