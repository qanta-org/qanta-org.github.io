---
layout: project
title: Adversarial Question Writing
description: "Human-in-the-loop generation of adversarial quiz bowl questions that stump computers but remain answerable by expert humans. Includes a live writing interface and ~1,000 question dataset."
venue: TACL 2019
year: 2019
badges: [dataset, interface]
authors: [eric-wallace, pedro-rodriguez, shi-feng, ikuya-yamada, jordan-boyd-graber]
---

# Adversarial Writing of Quiz Bowl Questions

This project accompanies the TACL 2019 paper *"Trick Me If You Can: Human-in-the-loop Generation of Adversarial Question Answering Examples"*, presented at ACL 2019 (Arsenale, Poster Session 3, July 26).

We develop questions specifically designed to stump computer QA systems while remaining answerable by expert human players. Question writers iterate in real time using live feedback from a QA system — the interface highlights words the AI finds informative, helping writers find clues that fool the machine.

## Interface

Write adversarial quiz bowl questions at **[write.qanta.org](http://write.qanta.org)**. The interface:
- Helps writers avoid obvious clues
- Highlights words the AI considers important
- Ensures questions work for both human and computer evaluation
- Reviews historical question patterns to avoid stock clues

## Data

From the [Data & Code](/data-and-code/) page, download:

- **Adversarial dataset** (~1,000 test questions): `qanta.tacl-trick.json`
- **Edit histories**: Full question development process (Google Drive)
- **Prelim & final questions** from the December 15, 2018 event (human-readable)
- **Prior version**: `qanta.advtest.2018.04.18.json`

A README explains all dataset field mappings.

## Citation

> Eric Wallace, Pedro Rodriguez, Shi Feng, Ikuya Yamada, Jordan Boyd-Graber.
> **Trick Me If You Can: Human-in-the-loop Generation of Adversarial Question Answering Examples.**
> *TACL 2019. Presented at ACL 2019.*

## Acknowledgements

System submission was made possible by an AWS research credit award from Amazon.

## Related

- [Stump a Computer](/stump-a-computer/) — try the live writing interface
- [2018 NeurIPS Competition](/competition/2018/) — the live event where these questions were used
