---
layout: article
title: Get Involved
description: Ways to contribute to QANTA through competitions, short-term event help, partnerships, and research projects.
permalink: /get-involved/
nav: false
nav_label: "Get Involved"
nav_order: 5
---

# Get Involved

There are many ways to contribute to QANTA — whether you're a researcher, quiz bowl player, question writer, educator, or sponsor.

<div class="alert alert-info" role="note">
  <strong>QANTA work is seasonal.</strong> We usually bring new people into research projects around the start of the academic semesters, near the end of August and in January. Competition work happens closer to each event, usually in the summer. If you reach out at another time and do not hear back, please try again during the next intake period.
</div>

## Compete

Sign up to play as a human team in our annual competition. We welcome quiz bowl players of all experience levels.

→ [Current competition details](/competition/2026/)

## Write Questions

Help us build better adversarial datasets. Our writing interface provides real-time feedback as you craft questions that stump AI systems.

→ [How to Stump a Computer](/stump-a-computer/) · [write.qanta.org](http://write.qanta.org)

## Help With a Tournament (One or Two Weeks)

Each competition needs a short burst of help immediately before and during the event. Depending on the tournament, this can include:

- Staffing or moderating games
- Testing the competition setup and improving participant instructions
- Editing questions or judging packets
- Importing questions, rosters, or results
- Recruiting players and spreading the word

These are event-specific roles rather than ongoing volunteer positions. The best time to ask is in the weeks leading up to a competition, usually in the summer.

## Research Projects

We take on new research collaborators near the beginning of each semester—typically in late August and January. Projects can involve coding, data collection, analysis, writing, or creative work. Most start with a small, self-contained tryout task so that you can see whether the work interests you and we can see how we work together.

Choose **one** project that fits your interests and current skills. Going deeply on one task is more useful than submitting several shallow attempts, and it is fine to switch after you have started. Project availability and exact tryout tasks change from one intake cycle to the next.

<details class="reveal-panel">
<summary>Updating QANTA ingestion <span>Data and coding</span></summary>

**What's the goal?**

Bring the QANTA dataset up to date with newer quiz bowl questions and create a more maintainable ingestion pipeline. This project combines document processing, data cleaning, and dataset engineering.

**What's the tryout project?**

Find a recent tournament not represented in QANTA and write a documented Python converter for its PDF or Word packets. The resulting records should separate question sentences, preserve packet metadata, and connect answers to canonical entities when possible.

**What would a publication look like?**

The full project could make ingestion repeatable, add browsing and search tools, publish regular dataset updates, evaluate current models, and support an updated dataset paper.

</details>

<details class="reveal-panel">
<summary>Writing and reading multimodal adversarial questions <span>Writing and hosting</span></summary>

**What's the goal?**

Create human–computer quiz bowl questions that remain fair and enjoyable for people while exposing weaknesses in AI systems. This project suits strong question writers, quiz bowl players, and people interested in hosting or communicating research.

**What's the tryout project?**

Either write a small set of pyramidal adversarial questions using text, images, or audio, or host and document a short online trivia game. The questions should feel natural to human players while remaining difficult for current systems.

**What would a publication look like?**

The larger collaboration would develop and edit more questions, run games, and analyze which clues challenge humans or computers. The output may be a dataset, event, or public-facing research artifact rather than a conventional machine-learning paper.

</details>

<details class="reveal-panel">
<summary>Turning question-answering lectures into a book <span>Research writing</span></summary>

**What's the goal?**

Turn existing lecture scripts and draft chapters into a coherent book about question answering. This is primarily a research-writing and technical-communication project. See the [question answering course](https://users.umiacs.umd.edu/~jbg/teaching/CMSC_848/) and [draft chapters on GitHub](https://github.com/Pinafore/questioning-aritifical-intelligence/tree/main/chapters).

**What's the tryout project?**

Revise one substantial chapter: update outdated material, add references, create or improve figures, and make sure the source compiles into a clean PDF.

**What would a publication look like?**

The full project would repeat that process across chapters and bring the collection together as a finished book rather than a conference paper.

</details>

<details class="reveal-panel">
<summary>Collecting trivia datasets with images and video <span>Data collection</span></summary>

**What's the goal?**

Find trivia and QA sources in which an image or video is necessary to answer the question, then convert them into a consistent, documented format. Most existing question-answering benchmarks are text-only.

**What's the tryout project?**

Build small extractors for a few different public sources. Each record should include the question, answer, category and other metadata, plus a stable reference to its media. The task is to demonstrate careful handling of several source formats, not to scrape entire websites.

**What would a publication look like?**

The full project could produce a multimodal trivia benchmark, evaluations of vision-language models, and a leaderboard measuring which questions and systems are genuinely challenging.

</details>

<details class="reveal-panel">
<summary>Editing human–computer game videos <span>Video and storytelling</span></summary>

**What's the goal?**

Turn recordings of adversarial human–computer trivia games into clear, engaging explanations of the research for a broader audience.

**What's the tryout project?**

Use selected footage to tell one short, understandable story: how a question was designed, how a person reasoned through it, or why a computer failed. Selection and framing matter more than using every clip or polishing every transition.

**What would the “real” output look like?**

The full project would produce finished videos from new competitions and make the research accessible beyond academic papers.

</details>

<details class="reveal-panel">
<summary>Collecting misinformation videos <span>Data and frontend coding</span></summary>

**What's the goal?**

Build a benchmark for misleading video headlines and links. A headline may misrepresent a manipulated clip or place a real video in the wrong context. The benchmark should challenge current vision-language models while remaining understandable to people.

**What's the tryout project?**

Collect and document a small set of in-context and out-of-context examples using an existing annotation tool and schema. Careful provenance, labels, and supporting metadata are essential; frontend experience can also help improve the collection interface.

**What would a publication look like?**

The full project would turn the annotations into training and evaluation data, add a human difficulty-ranking workflow, and develop systems for detecting misleading video context.

</details>

Interested in one of these projects? Email [Jordan Boyd-Graber](https://users.umiacs.umd.edu/~jbg/) at [{{ site.contact_email }}](mailto:{{ site.contact_email }}) near the next intake period. Mention the single project that most interests you and the experience you would bring to it.

## Research FAQ

<details class="reveal-panel reveal-panel-faq">
<summary>Should I try more than one project?</summary>

No. Pick one project and explore it in depth. It is fine to change direction if the first choice is not a good fit, but please do not submit several tryout projects at once.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Is the work paid or available for course credit?</summary>

Research collaborations are generally unpaid at first, although UMD students may be able to arrange course credit. Funding and credit depend on the project and semester, so confirm the details before committing.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Does everyone who completes a tryout join a project?</summary>

No. Capacity changes each semester based on the number of submissions, available projects, current group members, and graduate-student supervision. A strong tryout is not a guarantee that we will have room.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Can we meet before I choose or submit a tryout?</summary>

We usually cannot schedule individual meetings with everyone before tryouts. Specific questions by email are welcome, but part of the tryout is showing that you can make progress from a deliberately open-ended task.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Do I need to be at the University of Maryland?</summary>

No. Research can be done remotely. We may arrange optional in-person meetings for people near Maryland, but travel is not required.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>What is the time commitment?</summary>

Start dates have some flexibility. Active collaborators should expect a weekly group or project meeting and regular progress between meetings; some projects may meet more often.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Will this lead to a publication?</summary>

Many projects can contribute to a publication, dataset, book, video, or other public research output, but the format varies and publication is never guaranteed. Each description above explains the likely direction.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>Can I ask for a recommendation letter?</summary>

Recommendation letters come after sustained research work, not simply after joining or completing a tryout. For a research-focused program, Jordan generally needs to have seen the project through a complete write-up with preliminary results—ideally a submitted or submission-ready document—before he can write a meaningful letter. A paper does not need to have been accepted. If research is not central to the program you are applying to, explain that context when you ask.

</details>

<details class="reveal-panel reveal-panel-faq">
<summary>I reached out and heard nothing. Should I assume the answer is no?</summary>

Not necessarily. Requests sent outside the late-August or January intake periods are easy to miss because projects are already underway. Try again at the start of the next cycle and mention your earlier message.

</details>

## Partner With Us

We're looking for groups to collaborate with:

**Quiz Bowl Tournaments**
Who want to use computer support to create questions that are challenging for both humans and computers, or who are open to computer entrants in their events.

**Machine Learning Organizers**
Who are looking for an in-person competition to complement, for example, a workshop on machine learning.

**Computer Science Educators**
Who want to take part in a machine learning curriculum built around question answering that can lead to an engaging in-person event.

**Corporate Sponsors**
Who would like to support our educational programs and competitions.

## Contact

[{{ site.contact_email }}](mailto:{{ site.contact_email }})
