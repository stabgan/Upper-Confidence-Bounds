# Upper Confidence Bound (UCB)

A reinforcement learning solution to the multi-armed bandit problem, applied to ad click-through rate optimization.

## What It Does

Given 10 ads and 10,000 simulated user rounds, the UCB algorithm learns which ad maximizes clicks by balancing **exploration** (trying less-known ads) with **exploitation** (favoring high-performing ones).

At each round, the algorithm selects the ad with the highest upper confidence bound:

```
UCB(i) = avg(i) + sqrt( (3/2) * ln(n) / N(i) )
```

- **avg(i)** -- average reward of ad *i* so far
- **n** -- current round number
- **N(i)** -- number of times ad *i* has been selected

Ads with no selections yet are assigned infinite confidence, ensuring every ad gets tried at least once. Over time, the exploration bonus shrinks and the algorithm converges on the best ad.

## Dataset

`Ads_CTR_Optimisation.csv` -- 10,000 rows x 10 columns. Each row is a user round; each column is an ad. Values are binary (1 = click, 0 = no click). The file must be in the same directory as the scripts.


## Tech Stack

| | Tool | Purpose |
|---|---|---|
| 🐍 | Python 3 | Primary implementation |
| 📈 | Matplotlib | Histogram visualization |
| 🗂️ | Pandas | CSV data loading |
| 📉 | R | Alternative implementation (base R) |

## Getting Started

### Python

```bash
pip install matplotlib pandas
python upper_confidence_bound.py
```

### R

```bash
Rscript upper_confidence_bound.R
```

Both scripts output a histogram showing how often each ad was selected. The best-performing ad dominates the distribution.

## Project Structure

```
upper_confidence_bound.py   # Python implementation
upper_confidence_bound.R    # R implementation
Ads_CTR_Optimisation.csv    # Simulated CTR dataset
LICENSE                     # MIT License
README.md
```

## Known Issues

- The simulation uses a fixed dataset rather than a live reward signal -- this is a batch replay, not true online learning.
- Changing N or d beyond the dataset dimensions will cause index errors; the code now derives these from the CSV automatically.

## License

MIT
