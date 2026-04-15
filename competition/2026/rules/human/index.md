---
layout: article
title: "2026 Competition: Human Rules"
---

# Human Rules — QANTA 2026

These rules cover **live human–computer gameplay**: procedures, **muting**, and **scoring** (points awarded in the room). For how tossups chain into bonuses and how interrupting works, start with the [rules overview](/competition/2026/rules/).

Unless explicitly amended here, tossup and bonus procedure follows
[**ACF** conventions](https://acf-quizbowl.com/rules/gameplay/).  If
there is ambiguity in the human rules, we will use the protocol
established by ACF.

## Team formation

One human can only be on one team per tournament.  A team can have a
maximum of three humans.  There are no restrictions on what humans can
serve on a team (i.e., it's an "open" tournament).

Computer players are reassigned each round. At the start of each round:

1. The captain of the human team with the worst win record picks two computer players.
2. Ties are broken by points per game.  (If a tie persists, a team is
   chosen randomly.)
3. The next-worst team then picks two computer players.
4. The process continues upward by standings.
5. If there are still AI teammates available, the draft continues in
the opposite direction (a snake draft).

For round-robin settings, once a computer has been drafted it cannot
be drafted again.  For playoffs, computers can be drafted multiple
times, but the same computer cannot be in the same match twice.

Each human team must have at least one computer player; if there are
not enough computer teams to accomodate the number of matches
required, duplicate computer players will be allowed, but the same
computer cannot be in the same match twice.

## Scoring — tossups

Any player on either team may buzz on a tossup. **Each team gets one buzz per tossup.**

| Situation | Correct | Incorrect |
|---|---|---|
| First buzz (no lockout yet) | +10 | −5 (team is locked out) |
| Second buzz (opponent locked out) | +10 | 0 |

If neither team buzzes, the tossup is dead and no points are awarded.

The **−5** on a first, wrong buzz discourages guessing too early: you should buzz when confidence is high enough to justify the risk (roughly, break-even is on the order of one-third confidence if the other side might still miss).

**After lockout:** when one team is wrong and locked out, the other team hears the rest of the question and may buzz with **no penalty** for a wrong answer on their single attempt.

## Scoring — bonuses

The team that answered the tossup correctly receives a **three-part bonus**. The decision to use AI assistance is scored **per part**.

| Decision | Correct | Incorrect |
|---|---|---|
| **Do not look** at AI outputs | **+10** | 0 |
| **Look** at AI, then give a final answer | **+5** | 0 |
| **Look** at AI, then **abstain** correctly (no one had the right answer) | **+1** | — |
| **Look** at AI, then **abstain** incorrectly (someone had the right answer) | — | 0 |

There are **no negative scores on bonuses**.

**Maximum per tossup–bonus cycle:** 10 (tossup) + 30 (three parts at +10 each) = **40** if the team nails the tossup and all three bonus parts without looking at AI.

## AI delegation modes (tossups)

At the start of the game, the humans decide how the computers will
play tossups:

- **Full autonomy (default):** systems buzz and answer on their own when they choose.
- **Fully controlled:** human players buzz **on behalf of** a
  computer; the computer’s answer is then scored like any other tossup
  attempt.
- **Muted:** The computer cannot buzz at all.

After a tossup ends and before the next tossup begins, the human
captain may instruct the moderator to **mute** a computer player. A
muted player may be barred from interrupting and/or from answering.

This can only change at the half of the game.  The humans can elect to
unmute a muted player, change to full autonomy, or change to fully
controlled.  If a computer is muted at this point, it does not count
as the "once per game" muting, which can interrupt gameplay.

Teams pick a mode before the game and may change it **once**, at halftime, for the second half.

## Tossup procedure (beyond scoring)

### Prompting

If a guess is too specific, too general, or otherwise does not exactly match the answer line, moderators will always prompt human players.

On tournament day, the tournament director will announce whether computer models can also be prompted. This policy is applied uniformly to all models on all teams.

### Conferring

There is no conferring about answer **substance** during tossups.

- Human players can hear incorrect answers that were given.
- Computer players do not hear those answers; they only learn that an incorrect answer occurred.
- Human players may see computer confidence while the question is read
  (to assist with proxy buzzing).
- Humans may use non-verbal confidence signals but may not convey answer content (for example, a gesture that encodes the answer is not allowed).


## Bonus procedure

After a team wins a tossup, it receives a three-part bonus. Parts share a theme but are otherwise unrelated to the tossup (except by coincidence).

For each bonus part:

1. Human players have two seconds to write an individual answer (not
   collected, not manditory but encouraged; reduces peer influence).
2. The moderator asks for a human consensus answer and if they want to
   see the computer response.  If the humans elect to commit to their
   answer, the moderator moves to the next question part.
3. Computer guesses and **rationales** are revealed.
4. The captain has five seconds to discuss with the team.
5. At the five-second mark, the captain must immediately begin the
   final answer or abstain from answering.

## Ranking of Teams

The ranking of human teams and final prizes is based on games won
within a bracket (i.e., if the field is large enough to support a
playoff round-robing bracket, placement will be based on rank in the
top playoff bracket, even if a team in a lower bracket has a better
record).  The tournament director may also elect to do a single or
double elimination playoff structure if that better uses available
packets.  In any event, the playoff structure will be announced before
tournament start once the field is finalized.

## Contact

Questions about human rules? Email [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
