---
layout: competition
title: 2025 Competition
status: past
description: Results and analysis from the 2025 QANTA Human-AI Cooperative QA competition.
---

# 2025 Competition Results

<img src="{{ site.baseurl }}/assets/images/heroes/competition-2025.jpg" alt="QANTA 2025 Competition" class="img-fluid rounded mb-4" style="width:100%;">

QANTA 2025 featured in-person and online Human-AI cooperative play, plus an AI systems leaderboard and adversarial packet writing.

---

## Highlights

- **June 14 (in-person) winner:** Sara's Cias
- **June 21 (online) winner:** QB They Reader
- **Top AI system:** BlackRaven (Jaimie Carlson)
- **Most adversarial packet prize:** Stephen Pachucki

---

## Stats Reports

- In-Person: [QANTA_2025_Stats_June_14](http://users.umiacs.umd.edu/~ying/qb/2025_QANTA/QANTA_2025_Stats_June_14.html)
- Online: [QANTA_2025_Stats_June_21](http://users.umiacs.umd.edu/~ying/qb/2025_QANTA/QANTA_2025_Stats_June_21.html)
- AI (combined): [QANTA_2025_AI_Stats_Combined](http://users.umiacs.umd.edu/~ying/qb/2025_QANTA/QANTA_2025_AI_Stats_Combined.html)

These reports include player-level and team-level performance, AI contribution/trust metrics on bonuses, and per-packet analysis.

---

## Winners and Prize Money

### June 14, 2025 - Human Teams

1. **Sara's Cias (Team 3)** - $150  
   Sara DelVillano, Warren Grace, Haughton Neppl
2. **Kicking and Screaming (Team 5)** - $100  
   Irene Ying, Michael
3. **Inquizitive (Team 1)** - $50  
   Kartik Ravisankar

### June 21, 2025 - Human Teams

1. **QB They Reader (Team 2)** - $150  
   Mohit Nair, Nate Brown, Angelo Pan
2. **Dot Gimpel the File (Team 4)** - $100  
   Ankit Aggarwal, Nikhil Desai, Sinecio Morales
3. **Cinco Ranch Education (Team 1)** - $50  
   Alan Lee, Anthony Yin, Ruchir Kodihalli

### AI Builders (Combined)

1. **BlackRaven** (Jaimie Carlson) - $200
2. **RodeRunner** (Neel Mokaria) - $150
3. **Tigerclaw** (Amanvir Parhar) - $100
4. **Sphinx** (Parth Dua, Marek Suppa) - $50

### Packet Writers

Most adversarial question sets by packet-level analysis:

- Packet 3: Noah Sheidlower (Music)
- Packet 5: Jaimie Carlson (Spatial Reasoning)
- Packet 7: Jordan Boyd-Graber (house-written; not prize eligible)

House-written packets were not eligible for writer prize payouts. The writing prize was awarded to **Stephen Pachucki ($50)**.

---

## Most Adversarial Questions (Examples)

### Example 1: Rapper identity with decoy clues

A question with clues intentionally pointing toward nearby entities (e.g., Nas, Kanye West, Machiavelli, Tupac aliases) remained answerable for strong humans while triggering wrong high-confidence AI guesses.

Outcome:

- Humans successfully resolved the intended entity from the full clue chain.
- AI systems were frequently misled by early local associations.

### Example 2: Composer identification under musical detail

A music question referencing specific rhythmic and thematic motifs from multiple works by Clara Schumann created strong discrimination.

Outcome:

- Humans were often cautious and waited.
- AI systems produced confident wrong guesses (e.g., Franz Liszt, Frederic Chopin).

### Example 3: Magritte visual clue integration

A multimodal art question integrating textual clues and visual object references ("This is not ...", bowler hat imagery, and Magritte works) required compositional reasoning.

Outcome:

- Humans often converged to **apple** midway through the question.
- Multiple AI systems converged on incorrect alternatives (e.g., skull).

---

## AI-Misled Human Cases

The 2025 format allowed direct measurement of when AI suggestions shifted human teams from correct reasoning paths to incorrect final answers.

### Case A: Bruegel bonus (Peasant Wedding)

- Gold answer: **bowls**
- AI suggestions included: **loaves of bread**, **pies**
- Human teams were considering pies; confident AI guesses pushed final answers further away from the gold answer.

### Case B: Capital-city proximity bonus

- Gold answer: **Luxembourg City**
- AI suggestions included: **Bonn**, **Brussels**
- Teams that had discussed Luxembourg were pulled toward AI-suggested alternatives.

---

## Acknowledgments

Thanks to Eve Fleisig, Yu Hou, Maharshi Gor, Yoo Yeon Sung, Noah Sheidlower, and all participating writers, players, and system designers.

---

## Related Pages

- [Computer Teams](/competition/2025/computer-teams/)
- [Human Teams](/competition/2025/human-teams/)
- [Question Authors](/competition/2025/question-authors/)

---

## Contact

If a stats link appears broken or a result looks incorrect, contact [{{ site.contact_email }}](mailto:{{ site.contact_email }}).
