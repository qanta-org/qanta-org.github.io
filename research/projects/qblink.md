---
layout: project
title: QBLink
authors: [ahmed-elgohary, chen-zhao, jordan-boyd-graber]
description: "Sequential open-domain QA dataset with 18,644 multi-step sequences (56,000 Q&A pairs) built from quiz bowl tossups. Tests contextual reasoning across chains of related questions."
venue: EMNLP 2018
year: 2018
badges: [dataset]
---

# QBLink: Sequential Open-Domain Question Answering

QBLink is a dataset for sequential question answering where multiple related questions about the same topic are answered in sequence. It evaluates how well QA systems leverage context from previous questions and answers.

**18,644 sequences · 56,000 question–answer pairs**

## Dataset Structure

Each sequence contains:

| Field | Description |
|---|---|
| `id` | Sequence identifier |
| `tournament` | Quiz bowl tournament source |
| `lead-in` | Introductory sentence defining the topic |
| `category` | Subject area (History, Literature, Philosophy, etc.) |
| `sub-category` | More specific classification |
| Questions 1–3 | Each with `question_text`, `raw_answer`, `wiki_page` |

Example sequences cover topics such as Bitcoin's inventor or Ronald Reagan's presidency, where later questions reference earlier answers to test contextual reasoning.

## Citation

> Ahmed Elgohary, Chen Zhao, Jordan Boyd-Graber.
> **Dataset and Baselines for Sequential Open-Domain Question Answering.**
> *EMNLP 2018.*

