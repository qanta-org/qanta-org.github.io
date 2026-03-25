---
layout: article
title: How to Stump a Computer
description: Guide to writing adversarial quiz bowl questions that fool AI systems while remaining fair to expert humans.
permalink: /stump-a-computer/
nav: true
nav_order: 4
nav_label: "How to Stump a Computer"
---

# How to Stump a Computer

The goal of this page is to provide information to help you write better adversarial questions.

Can you write a question that a top computer QA system can't answer — but an expert human can? Write using our adversarial interface at **[write.qanta.org](http://write.qanta.org)**. The interface provides real-time feedback as you type: words the AI considers important are highlighted, helping you craft clues that fool the machine while remaining fair to expert humans.

---

## What Makes a Question Adversarial?

Good adversarial questions use one or more of these strategies:

- **Paraphrased content** — avoid phrasing that directly echoes standard training text; rephrase well-known facts in ways that require understanding, not retrieval
- **Logical and multi-hop reasoning** — require the reader to chain multiple facts together rather than recall a single association
- **Commonsense or domain expertise** — draw on knowledge that is tacit for experts but absent from typical QA training data
- **Mathematical components** — include a calculation or quantity reasoning step the AI must solve correctly
- **Cross-lingual elements** — use names, terms, or wordplay from other languages that require language knowledge beyond English

These are starting points — creativity is the most important ingredient.

---

## What Makes a Question Bad?

The following patterns produce questions that look adversarial but are actually flawed. Examples are drawn from a quiz game called *Spiel des Wissens*.

### Ambiguous answers

> *"What is the name of the literary genre in which elements of the real and the magical world are interwoven?"*

This question has multiple defensible answers — "fairy tales," "fantasy," and "magical realism" are all reasonable. A question is bad if a knowledgeable person could argue for more than one answer.

### Vague location or scope

> *"Where are the Virunga Volcanoes?"*

"Where" could mean Earth, Africa, Central Africa, or the Democratic Republic of Congo. The intended answer must be unambiguous. Similarly:

> *"Where was the first Iron Man?"*

This is unclear without specifying whether "Iron Man" refers to the Marvel film, a triathlon, or something else.

### False presuppositions

> *"What color are flamingo feathers?"*

Flamingo feather color depends on diet — flamingos raised without carotenoids are white. A question that assumes a false fact about its subject is flawed regardless of how well-known the misconception is.

> *"What voltage comes out of the socket?"* &nbsp; *"What connector do you use to charge a phone?"*

Both vary by country and device. Questions that assume a universal answer where none exists are problematic.

### Subjective qualifiers

> *"What's the name of Christopher Columbus's most famous ship?"*

"Most famous" is subjective and contested. Adding qualifiers like "most famous," "best," or "greatest" introduces ambiguity that the AI can exploit and that unfairly penalizes knowledgeable humans who know the debate.

### Unclear pronoun references

> *"What famous novel takes place in an Italian Benedictine Abbey?"*

If a question uses "it," "this," or "the work" without establishing what type of thing the answer is (a novel, a person, a place), a reader cannot immediately verify their answer. Always make the answer type clear early in the question.

---

## What Makes a Question Good?

Ask yourself: **could a human with perfect information produce a certificate to their answer?** If not, the question is too vague.

A well-constructed adversarial question satisfies both of these criteria simultaneously:

1. **A knowledgeable human immediately recognizes the correct answer.** Once they have the answer in mind, they can check whether it's correct relatively quickly — the "puzzle pieces fit together" moment.
2. **The AI system fails to answer correctly.** Ideally, the system is confidently wrong, not simply confused.

The question:

> *"Who was the last Czar of Russia?"*

is an example of a question that is clear and answerable — but not adversarial, because it's easy for AI. Your goal is to maintain that clarity while adding the properties above (paraphrase, reasoning, expertise) that trip up the machine.

**Difficulty target:** Questions should be at least "2-dot" difficulty — roughly equivalent to high school nationals (HSNCT). The first one or two lines of the question should be unanswerable by a baseline AI system.

**Answer format:** Answers should match Wikipedia page titles when possible. Redirects and common alternate names are accepted.

---

## Questions about Question Writing

**How difficult should the questions be?**

Questions should range from fairly accessible for experienced trivia players to genuinely challenging. A reasonable benchmark is high school nationals (HSNCT) difficulty. The system should not be able to answer from the first clue alone.

**What computers should not be able to answer the questions?**

It's acceptable — even desirable — if different AI systems fail in different ways. The goal is not to defeat one specific system but to find clues that systematically expose the limits of language model reasoning.

**I can't find my favorite answer in the system. Why is this?**

The answer database includes only answers that appear in mainstream quiz bowl tournaments. This ensures that when a computer fails, it's because of a comprehension gap — not because the answer was never in its training data. If your answer isn't recognized, try an alternate Wikipedia page title.

**How do I make an account on the interface?**

Just log in with a new email and password. This will create a new account automatically.

**What if I forget my password?**

Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}) and we'll help you recover access.

**What are the strange highlighted colors in the interface?**

Words that are highlighted are "important" for our Quizbowl AI system to make its predictions. If you modify those words, there is a high chance the system will get more confused. Use the highlights as a guide — if the AI is latching onto a specific phrase, rephrase it.

**Do I have to use a Wikipedia page title as the answer?**

Answers should match Wikipedia page titles when possible. Non-standard answers are sometimes acceptable, but using the Wikipedia title ensures the computer is penalized for a comprehension failure rather than a lookup failure.

---

## Get Started

Write adversarial questions at **[write.qanta.org](http://write.qanta.org)**.

For background on the research behind this interface, see the [Adversarial QA project page](/research/projects/adversarial/). To submit questions to an upcoming competition, see the [current competition](/competition/2026/).
