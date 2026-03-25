---
layout: article
title: DELFT
description: "Factoid QA system combining knowledge graph and free-text reasoning via graph neural networks over Wikipedia. Outperforms BERT-based baselines on entity-rich questions."
venue: WWW 2020
year: 2020
badges: [system, dataset]
---

# DELFT: Complex Factoid QA with a Free-Text Knowledge Graph

DELFT is a factoid question answering system that combines the nuance and depth of knowledge graph QA with the broader coverage of free text. It builds a free-text knowledge graph from Wikipedia — entities as nodes, co-occurrence sentences as edges — and uses a graph neural network to reason over it.

## Approach

DELFT constructs dense semantic graphs and employs graph neural networks to combine node evidence through edge sentences to determine answers. This hybrid approach outperforms pure machine reading and BERT-based baselines on entity-rich questions.

## Wikipedia Graph Data

Two versions are provided:

| Version | Description | Download |
|---|---|---|
| Original links | Wikipedia article hyperlinks as edges | [enwiki_links_anchor_1101.zip](https://obj.umiacs.umd.edu/delft_wiki_graph/enwiki_links_anchor_1101.zip) |
| TagMe entities | Entity annotations via TagME as edges | [wiki_anchor_1101.zip](https://obj.umiacs.umd.edu/delft_wiki_graph/wiki_anchor_1101.zip) |

Each entry contains: page id, title, text, anchored entities (from TagMe or article links).

## Resources

- **Paper**: [Complex Factoid Question Answering with a Free-Text Knowledge Graph](http://users.umiacs.umd.edu/~chenz/files/2020_www_graph_qa.pdf) — WWW 2020
- **Code**: [github.com/henryzhao5852/DELFT](https://github.com/henryzhao5852/DELFT)
- **Graph info**: [github.com/henryzhao5852/DELFT/tree/master/wiki_graph](https://github.com/henryzhao5852/DELFT/tree/master/wiki_graph)

## Citation

```
@inproceedings{Zhao:Xiong:Qian:Boyd-Graber-2020,
  Title  = {Complex Factoid Question Answering with a Free-Text Knowledge Graph},
  Author = {Chen Zhao and Chenyan Xiong and Xin Qian and Jordan Boyd-Graber},
  Booktitle = {The Web Conference},
  Year   = {2020}
}
```

## Contact

Chen Zhao — chenz@cs.umd.edu
