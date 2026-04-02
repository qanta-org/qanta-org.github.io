---
layout: article
title: What's a Pyramidal Adversarial Question
description: Guide to writing pyramidal adversarial quiz bowl questions that fool AI systems while remaining fair to expert humans.
permalink: /stump-a-computer/
nav: true
nav_order: 4
nav_label: "What's a Pyramidal Adversarial Question"
---

# What's a Pyramidal Adversarial Question

Can you write a question that a top computer QA system cannot answer - but an expert human can?

Write using our adversarial interface at **[write.qanta.org](http://write.qanta.org)**. The interface provides real-time feedback as you type.

## Jump to a Section

- [Section 1: Why Pyramidal Questions](#section-1-why-pyramidal-questions)
- [Section 2: Why Adversarial Questions](#section-2-why-adversarial-questions)
- [Section 3: Multimodal](#section-3-multimodal)
- [Section 4: Anti-Patterns](#section-4-anti-patterns)
- [Section 5: Advice for Text-Based Questions](#section-5-advice-for-text-based-questions)
- [Section 6: Advice for Multimodal Questions](#section-6-advice-for-multimodal-questions)

---

## Section 1: Why Pyramidal Questions

Pyramidal questions are designed to reward deep knowledge, not reflexes or keyword matching.

In quiz bowl, a good question starts with hard clues and then progressively becomes easier. This format is useful for AI evaluation because it tests whether a system can reason from nuanced evidence early, not just recover the answer from a late giveaway clue.

From [Quizbowl: The Case for Incremental Question Answering](https://arxiv.org/abs/1904.04792):

- Incremental answering better separates skill across both humans and machines.
- It introduces a decision problem: not just "what is the answer," but also "when should I answer?"
- It makes calibration matter: strong systems should know when they are likely correct.

Practical takeaway: write clues that are uniquely identifying when combined, and place easier clues later.

---

## Section 2: Why Adversarial Questions

Adversarial questions are useful because standard benchmarks can be solved with shallow patterns. Adversarial writing helps expose where models fail despite strong leaderboard performance.

From [Trick Me If You Can](https://aclanthology.org/Q19-1029/):

- Human-in-the-loop writing produces richer and more diverse failure cases than automatic perturbations.
- Questions can remain natural and answerable for humans while still stumping strong neural and IR baselines.
- Adversarial questions reveal weaknesses such as multi-hop reasoning failures and entity-type confusion.

Practical takeaway: target model weaknesses while keeping the question fair and answerable for knowledgeable humans.

---

## Section 3: Multimodal

Multimodal adversarial questions combine text with images (and potentially audio/video) so that solving requires integrating evidence across modalities.

Why this matters:

- There have been multimodal quizbowl tournaments before, but many were not deeply integrated across modalities.
- In some audio formats, the question is effectively "name the country of the composer," followed by a sequence of audio clips.
- In some image formats, the question is effectively "name the film," followed by a sequence of stills.

Our goal is different:

- Clues still move from harder to easier, as in standard pyramidal writing.
- But clues should be interleaved across modalities, not grouped as "all text then all images" (or vice versa).
- The answer should emerge from how text and media clues interact over time.

This interleaved multimodal pyramidal style is new as an evaluation target for both computer QA and human QA.

---

## Section 4: Anti-Patterns

These make questions hard in a bad way (they do not test skill):

### Ambiguous answers

A question is flawed if multiple answers are defensible for an expert.

### Vague scope

Questions like "Where is X?" can have many correct granularities (country, region, city).

### False presuppositions

Do not bake incorrect assumptions into the prompt.

### Subjective qualifiers

Avoid "most famous," "best," or "greatest" unless the criterion is explicit.

### Unclear answer type

Make the expected answer type clear early (person, place, work, concept, etc.).

---

## Section 5: Advice for Text-Based Questions

- Keep pyramidal structure: hard clues first, easier clues later.
- Prefer paraphrase and composition over copied canonical phrasing.
- Force multi-hop reasoning where possible.
- Ensure a human with strong domain knowledge can verify the answer quickly once they see it.
- Aim for questions that are challenging but fair (roughly high school nationals level or above).
- Use accepted answer formats (prefer Wikipedia page titles when possible).

A useful check: could a strong human explain exactly why each clue points to the answer?

---

## Section 6: Advice for Multimodal Questions

General guidelines:

- Do not rely on a famous image in its original form; many models may have already seen it.
- Instead, use transformations: crop, annotate, recompose, redraw, or lightly edit.
- Make sure the question cannot be solved from text alone.
- Make sure the question cannot be solved from image alone.
- Require cross-modal reasoning: the text should disambiguate the image, and the image should disambiguate the text.

Example pattern:

- Weak pattern: "What religion was George Romney?" plus a recognizable photo where text alone already gives the answer.
- Better pattern: a photo of George Romney at a march plus textual clues that require identifying the event context and then connecting that context to the final answer.

---

## Get Started

Write adversarial questions at **[write.qanta.org](http://write.qanta.org)**.

For background on this line of work, see the [Adversarial QA project page](/research/projects/adversarial/). To submit questions to an upcoming competition, see the [current competition](/competition/2026/).
