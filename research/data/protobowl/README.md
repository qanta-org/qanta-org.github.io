# Protobowl Data

This directory contains normalized data derived from Protobowl logs for research use.

The data in this directory was used in work including:

- [Opponent Modeling](https://arxiv.org/abs/1904.04792)
- [Quiz Bowl: The Case for Incremental Question Answering](https://arxiv.org/abs/1609.05559)

The Protobowl approach itself began with:

- [Besting the Quizmaster](https://aclanthology.org/D12-1118/)

That work deployed the first interface that tracked people playing quiz bowl online.

We are especially grateful to Kevin Kwok for providing the data, and to all of the players who contributed to the dataset.

# Protobowl Data Manifest

This directory contains normalized Protobowl-derived research data and helper files.

## Files

- `protobowl-questions.json`: question metadata keyed by normalized `question_id`
- `protobowl-buzz-ratios.svg`: histogram of `buzz_position_ratio_time`
- `protobowl-buzzes-sample.json`: small uncompressed sample of grouped user buzz records for quick inspection
- `buzzes/protobowl-buzzes-by-user-<letter>.json.gz`: 26 gzipped shards of grouped buzz records, where each user is assigned to a shard by hashing the UID and mapping it onto `a` through `z`
- `unzip_buzz_shards.sh`: helper script to decompress all shard files in place

## Sharding

Each user is assigned to exactly one shard by hashing the user UID and taking the result modulo 26. This keeps all of a user's buzz records together while splitting the overall dataset into more manageable files.

## Decompression

The main buzz outputs are written as gzipped JSON files to reduce disk usage. To decompress all shards, run:

```bash
bash unzip_buzz_shards.sh
```