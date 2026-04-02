---
layout: overview
title: Data & Code
description: Competition code, QANTA datasets, and paper-specific code/data resources.
permalink: /data-and-code/
nav: true
nav_label: "Data & Code"
nav_order: 4
---

# Data & Code

A single place for starter code, core QANTA datasets, and paper-specific resources.

---

## Competition / Tutorial Code

The best way to quickly get started with these data and this format is to use the CodaLab starter system and run it locally.

| Resource | Link | Description |
|---|---|---|
| Competition baseline | [Pinafore/qanta-codalab]({{ site.github.codalab }}) | Simplified system for quick setup, inspection, and leaderboard submission |
| Full research codebase | [Pinafore/qb]({{ site.github.main }}) | Main QA system used in exhibition matches and research prototypes |
| Leaderboard | [CodaLab](https://codalab.lisn.upsaclay.fr/) | Submit and compare systems |

---

## QANTA Data

Computer-friendly data derived directly from quiz bowl data:

- Normal Questions
- Human responses
- Naturalized Questions
- Adversarial Questions (in the same format as the normal questions)

| Data Direct Download | Huggingface Link | Description | Code |
|---|---|---|---|
| [QANTA main datasets](/research/datasets/) | - | Canonical QANTA question data and related dataset docs | [Pinafore/qb]({{ site.github.main }}) |
| - | [Quizbowl human responses](https://huggingface.co/collections/mgor/quizbowl-66f8541f46d413c380669551) | Human answer traces and response behavior data | [maharshi95/neural-irt](https://github.com/maharshi95/neural-irt) |
| - | - | Naturalized questions derived from trivia-style QA | [Pinafore/qb2nq](https://github.com/Pinafore/qb2nq) |
| [Adversarial questions JSON](../downloads/2019_tacl_trick.json) | - | Adversarial examples in compatible QA format | [Eric-Wallace/trickme-interface](https://github.com/Eric-Wallace/trickme-interface) |

---

## Code / Data from Papers

| Paper | Data Direct Download | Huggingface Link | Description | Code |
|---|---|---|---|---|
| [Reverse Question Answering: Can an LLM Write a Question so Hard (or Bad) that it Can't Answer?](http://cs.umd.edu/~jbg//docs/2025_naacl_reverseqa.pdf) | - | - | NAACL 2025 | - |
| [GRACE: A Granular Benchmark for Evaluating Model Calibration against Human Calibration](http://cs.umd.edu/~jbg//docs/2025_acl_grace.pdf) | - | - | ACL 2025 calibration benchmark | [yysung/advcalibration](https://github.com/yysung/advcalibration) |
| [No Questions are Stupid and but some are Poorly Posed: Understanding Poorly-Posed Information-Seeking Questions](http://cs.umd.edu/~jbg//docs/2025_acl_badq.pdf) | - | - | ACL 2025 question quality | [nehasrikn/poorly-posed-questions](https://github.com/nehasrikn/poorly-posed-questions) |
| [Which of These Best Describes Multiple Choice Evaluation with LLMs? A) Forced B) Flawed C) Fixable D) All of the Above](http://cs.umd.edu/~jbg//docs/2025_acl_mcqa_bad.pdf) | - | - | ACL 2025 evaluation methods | - |
| [ADVSCORE: A Metric for the Evaluation and Creation of Adversarial Benchmarks](http://cs.umd.edu/~jbg//docs/2025_naacl_advscore.pdf) | - | - | NAACL 2025 adversarialness metric | - |
| [Do great minds think alike? Investigating Human-AI Complementarity in Question Answering with CAIMIRA](http://cs.umd.edu/~jbg//docs/2024_emnlp_caimira.pdf) | - | [Quizbowl collection](https://huggingface.co/collections/mgor/quizbowl-66f8541f46d413c380669551) | EMNLP 2024 complementarity | [maharshi95/neural-irt](https://github.com/maharshi95/neural-irt) |
| [You Make me Feel like a Natural Question: Training QA Systems on Transformed Trivia Questions](http://cs.umd.edu/~jbg//docs/2024_emnlp_natural.pdf) | - | - | EMNLP 2024 naturalized QA | [Pinafore/qb2nq](https://github.com/Pinafore/qb2nq) |
| [PEDANTS (Precise Evaluations of Diverse Answer Nominee Text for Skinflints): Use Evaluation Metrics Wisely---Efficient Evaluation Analysis and Benchmarking for Open-Domain Question Answering](https://arxiv.org/abs/2402.11161) | - | - | EMNLP Findings 2024 evaluation | [zli12321/PEDANTS-LLM-Evaluation](https://github.com/zli12321/PEDANTS-LLM-Evaluation) |
| [Automatic Explicitation to Bridge the Background Knowledge Gap in Translation and its Evaluation with Multilingual QA](http://cs.umd.edu/~jbg//docs/2023_emnlp_explicitation.pdf) | - | - | EMNLP 2023 translation and QA | - |
| [Learning to Explain Selectively: A Case Study on Question Answering](http://cs.umd.edu/~jbg//docs/2022_emnlp_augment.pdf) | [Data](https://bit.ly/selective_explanation) | - | EMNLP 2022 explanations | - |
| [SimQA: Detecting Simultaneous MT Errors through Word-by-Word Question Answering](http://cs.umd.edu/~jbg//docs/2022_emnlp_simqa.pdf) | - | - | EMNLP 2022 simultaneous MT QA | [SimQA code](https://go.umd.edu/simqa) |
| [Cheater's Bowl: Human vs. Computer Search Strategies for Open-Domain QA](http://cs.umd.edu/~jbg//docs/2022_emnlp_cheaters.pdf) | [Data](../../downloads/cheater_data.zip) | - | EMNLP Findings 2022 | [Code](../../downloads/cheater_code.zip) |
| [Re-Examining Calibration: The Case of Question Answering](http://cs.umd.edu/~jbg//docs/2022_emnlp_calibration.pdf) | - | - | EMNLP Findings 2022 calibration | [NoviScl/calibrateQA](https://github.com/NoviScl/calibrateQA) |
| [Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?](http://cs.umd.edu/~jbg//docs/2021_acl_leaderboard.pdf) | [Data](http://irt.pedro.ai) | - | ACL 2021 leaderboard analysis | [leaderboard.pedro.ai](https://leaderboard.pedro.ai/) |
| [Distantly-Supervised Dense Retrieval Enables Open-Domain Question Answering without Evidence Annotation](http://cs.umd.edu/~jbg//docs/2021_emnlp_weak_dpr.pdf) | - | - | EMNLP 2021 dense retrieval | [henryzhao5852/DistDR](https://github.com/henryzhao5852/DistDR) |
| [Evaluation Paradigms in Question Answering](http://cs.umd.edu/~jbg//docs/2021_emnlp_paradigms.pdf) | - | - | EMNLP 2021 paradigm framing | - |
| [Toward Deconfounding the Influence of Subject's Demographic Characteristics in Question Answering](http://cs.umd.edu/~jbg//docs/2021_emnlp_qa_fairness.pdf) | - | - | EMNLP 2021 fairness | - |
| [What's in a Name? Answer Equivalence For Open-Domain Question Answering](http://cs.umd.edu/~jbg//docs/2021_emnlp_answer_equiv.pdf) | - | - | EMNLP 2021 answer equivalence | - |
| [Multi-Step Reasoning Over Unstructured Text with Beam Dense Retrieval](http://cs.umd.edu/~jbg//docs/2021_naacl_multi_ance.pdf) | - | - | NAACL 2021 multistep retrieval | - |
| [Complex Factoid Question Answering with a Free-Text Knowledge Graph](http://cs.umd.edu/~jbg//docs/2020_www_delft.pdf) | - | - | WWW 2020 free-text KG QA | [henryzhao5852/DELFT](https://github.com/henryzhao5852/DELFT) |
| [Meta Answering for Machine Reading](https://arxiv.org/abs/1911.04156) | - | - | ArXiv 2020 machine reading | - |
| [Quizbowl: The Case for Incremental Question Answering](https://arxiv.org/abs/1904.04792) | - | - | ArXiv 2020 incremental QA | [QANTA site](http://www.qanta.org) |
| [What Question Answering can Learn from Trivia Nerds](http://cs.umd.edu/~jbg//docs/2020_acl_trivia.pdf) | - | - | ACL 2020 perspective paper | - |
| [Mitigating Noisy Inputs for Question Answering](http://cs.umd.edu/~jbg//docs/2019_interspeech_asr) | - | - | Interspeech 2019 noisy QA inputs | - |
| [Can You Unpack That? Learning to Rewrite Questions-in-Context](http://cs.umd.edu/~jbg//docs/2019_emnlp_sequentialqa.pdf) | [Data](http://canard.qanta.org) | - | EMNLP 2019 question rewriting | [aagohary/canard](https://github.com/aagohary/canard) |
| [What AI can do for me: Evaluating Machine Learning Interpretations in Cooperative Play](http://cs.umd.edu/~jbg//docs/2019_iui_augment.pdf) | - | - | IUI 2019 interpretability in play | - |
| [Trick Me If You Can: Human-in-the-loop Generation of Adversarial Question Answering Examples](http://cs.umd.edu/~jbg//docs/2019_tacl_trick.pdf) | [Data](../downloads/2019_tacl_trick.json) | - | TACL 2019 adversarial QA | [Eric-Wallace/trickme-interface](https://github.com/Eric-Wallace/trickme-interface) |

---

## Contact

For dataset access or questions: [{{ site.contact_email }}](mailto:{{ site.contact_email }})
