---
layout: article
title: "2026 Competition: Rules"
---

# Rules — QANTA 2026

This page is the official source of truth for QANTA 2026 gameplay rules, scoring, and procedures.

## Game Structure

Each match is played between **two teams**. A game consists of **20 tossup-bonus cycles** split into two halves of 10. Each cycle follows the same pattern:

1. A **tossup** is read (all players race to buzz)
2. The team that answers the tossup correctly earns a **bonus** (three parts)

Each team consists of **human players and two AI models**.

---

## Tossups

Tossup questions are read word by word. Any player on either team — human or AI — may buzz in at any point. **Each team gets one buzz per tossup** (once any player on a team buzzes, the entire team is committed to that answer).

### Scoring

| Situation | Correct | Incorrect |
|---|---|---|
| First buzz (no lockout) | +10 | -5 (team is locked out) |
| Second buzz (opponent locked out) | +10 | 0 |

If neither team buzzes, the question is dead and no points are awarded.

**Why the -5 penalty?** It prevents teams from buzzing on the first word and guessing. You should buzz when you are reasonably confident — the break-even is about 33% confidence.

**After lockout:** when one team buzzes incorrectly and is locked out, the remaining team hears the rest of the question and can buzz with no penalty for a wrong answer.

---

## AI Delegation Modes

Before each half, teams choose how their AI models participate on tossups. There are three modes:

### Full Autonomy (default)

AI models buzz and answer on their own whenever they are confident. The team has no direct control over when AI buzzes.

### Semi-Autonomous

The team sets a **token threshold** — a position in the question before which AI models are not allowed to buzz. After that point, AI models buzz autonomously.

*Example: setting a threshold of 20 means AI models stay silent for the first 20 tokens of each question, then can buzz freely from token 21 onward.*

This lets teams prevent early AI buzzes on thin evidence while still benefiting from AI speed on later clues.

### Fully Controlled

Human players buzz **on behalf of** the AI models. When a human triggers an AI buzz, the AI model's answer is submitted and scored normally (+10/-5 or +10/0).

This gives maximum control but requires human attention — the player must monitor AI confidence while also processing the question.

### Changing Modes

Teams choose a delegation mode before the game starts. **The mode can be changed exactly once**, at halftime (after the 10th tossup-bonus cycle). The new mode applies for the entire second half.

---

## Bonuses

The team that answers a tossup correctly receives a **bonus question with three parts**. Bonuses test the team's ability to use — or choose not to use — AI assistance.

### Flow (per part)

1. Humans give their initial answer
2. Humans decide: **look at AI responses** or **don't look**
3. Based on that decision, scoring differs

### Scoring

The decision to look or not is made **independently for each part**.

<div class="table-responsive">

| Decision | Correct | Incorrect |
|---|---|---|
| **Don't look** at AI | **+15** | 0 |
| **Look** at AI, give final answer | **+10** | 0 |
| **Look** at AI, abstain correctly (nobody had the right answer) | **+5** | — |
| **Look** at AI, abstain incorrectly (someone had the right answer) | — | 0 |

</div>

### How to Read This

- **Not looking** rewards pure human knowledge with the highest possible score (+15). There is no penalty for a wrong answer.
- **Looking** at AI responses gives the team more information but caps the score at +10. Again, no penalty for a wrong answer.
- **Abstaining** after looking means the team believes neither their original answer nor the AI's answer is correct. If they are right about that, they earn +5 for correctly identifying bad answers. If they are wrong (someone actually had it), they get 0.

### Why This Structure Works

The +15/+10/+5 tiers create a genuine strategic decision:

- **Strong teams** on a topic should skip AI — the +15 premium rewards confidence in human knowledge.
- **Uncertain teams** should look at AI — the +10 payoff plus AI information often beats gambling on +15.
- **Abstaining** is a real third option that rewards the skill of evaluating answer quality, not just knowing answers.

There are **no negative scores on bonuses**. The cost of using AI is purely opportunity cost (15 → 10 max), not a direct penalty.

---

## Drafting

AI models are assigned to teams through a draft system.

### Round 1

AI models are **randomly assigned** to teams before the first round.

### Subsequent Rounds — Serpentine Draft

Between rounds, teams draft AI models in a **serpentine** (snake) order based on current standings:

1. The **lowest-scoring team** picks first
2. Picks continue upward to the **highest-scoring team**
3. The highest-scoring team picks **twice** (the turn of the snake)
4. Picks continue back down to the lowest-scoring team

Each team drafts **two AI models** per round. The serpentine structure gives trailing teams first choice of the best-performing models, helping to keep matches competitive.

*Example with 4 teams (ranked 1st to 4th):*
*Pick order: 4th → 3rd → 2nd → 1st → 1st → 2nd → 3rd → 4th*

---

## Quick Reference

| Element | Scoring |
|---|---|
| Tossup — correct (first buzz) | +10 |
| Tossup — incorrect (first buzz) | -5 |
| Tossup — correct (after lockout) | +10 |
| Tossup — incorrect (after lockout) | 0 |
| Bonus — correct, no AI | +15 |
| Bonus — correct, with AI | +10 |
| Bonus — correct abstain | +5 |
| Bonus — incorrect (any mode) | 0 |

**Maximum points per cycle:** 10 (tossup) + 45 (bonus, 3 parts at +15) = **55**

---

## Contact

Questions about the rules? Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
