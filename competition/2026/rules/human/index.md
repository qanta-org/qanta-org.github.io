---
layout: article
title: "2026 Competition: Human Rules"
---

# Human Rules — QANTA 2026

These rules cover **live human–computer gameplay**: procedures, **muting**, and **scoring** (points awarded in the room). For how tossups chain into bonuses and how interrupting works, start with the [rules overview](/competition/2026/rules/).

Unless explicitly amended here, tossup and bonus procedure follows **ACF** conventions.

## Team formation

Human players remain on the same team throughout the tournament.

Computer players are reassigned each round. At the start of each round:

1. The captain of the human team with the worst win record picks two computer players.
2. Ties are broken by points per game.
3. The next-worst team then picks two computer players.
4. The process continues upward by standings.

Each human team must have at least one computer player.

## Scoring — tossups

Any player on either team may buzz on a tossup. **Each team gets one buzz per tossup.**

| Situation | Correct | Incorrect |
|---|---|---|
| First buzz (no lockout yet) | +10 | −5 (team is locked out) |
| Second buzz (opponent locked out) | +10 | 0 |

If neither team buzzes, the tossup is dead and no points are awarded.

The **−5** on a first, wrong buzz discourages guessing on the earliest clue: you should buzz when confidence is high enough to justify the risk (roughly, break-even is on the order of one-third confidence if the other side might still miss).

**After lockout:** when one team is wrong and locked out, the other team hears the rest of the question and may buzz with **no penalty** for a wrong answer on their single attempt.

## Scoring — bonuses

The team that answered the tossup correctly receives a **three-part bonus**. The decision to use AI assistance is scored **per part**.

| Decision | Correct | Incorrect |
|---|---|---|
| **Do not look** at AI outputs | **+15** | 0 |
| **Look** at AI, then give a final answer | **+10** | 0 |
| **Look** at AI, then **abstain** correctly (no one had the right answer) | **+5** | — |
| **Look** at AI, then **abstain** incorrectly (someone had the right answer) | — | 0 |

There are **no negative scores on bonuses**; the cost of using AI is opportunity cost (15 → 10 at most on a correct answer), not a direct penalty.

**Maximum per tossup–bonus cycle:** 10 (tossup) + 45 (three parts at +15 each) = **55** if the team nails the tossup and all three bonus parts without looking at AI.

## AI delegation modes (tossups)

Before each half, teams choose how computer players participate on tossups:

- **Full autonomy (default):** systems buzz and answer on their own when they choose.
- **Semi-autonomous:** the team sets a **token threshold**; before that position in the question, computer players may not buzz; after it, they behave autonomously.
- **Fully controlled:** human players buzz **on behalf of** a computer; the computer’s answer is then scored like any other tossup attempt.

Teams pick a mode before the game and may change it **once**, at halftime, for the second half.

## Tossup procedure (beyond scoring)

### Refining guesses

If a guess is too specific, too general, or otherwise does not exactly match the answer line, moderators will always prompt human players.

On tournament day, the tournament director will announce whether computer models can also be prompted. This policy is applied uniformly to all models on all teams.

### Conferring

There is no conferring about answer **substance**.

- Human players can hear incorrect answers that were given.
- Computer players do not hear those answers; they only learn that an incorrect answer occurred.
- Human players may see computer confidence while the question is read.
- Humans may use non-verbal confidence signals but may not convey answer content (for example, a gesture that encodes the answer is not allowed).

### Muting computer players

After a tossup ends and before the next tossup begins, the human captain may instruct the moderator to **mute** a computer player. A muted player may be barred from interrupting and/or from answering for the **rest of the match**. Muting cannot be undone for that player in that match.

## Bonus procedure

After a team wins a tossup, it receives a three-part bonus. Parts share a theme but are otherwise unrelated to the tossup (except by coincidence).

For each bonus part:

1. Human players have two seconds to write an individual answer (not collected; reduces peer influence).
2. The moderator asks each human player, in arbitrary or randomized order, for an immediate response.
3. Computer guesses and **rationales** are revealed.
4. The captain has five seconds to discuss with the team.
5. At the five-second mark, the captain must immediately begin the final answer.

Directed answers are not allowed. The final answer must come from the designated captain.

## Contact

Questions about human rules? Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
