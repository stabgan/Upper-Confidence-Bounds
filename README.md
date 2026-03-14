# Upper Confidence Bound (UCB)

A reinforcement learning solution to the multi-armed bandit problem, applied to ad click-through rate optimization.

## What It Does

Given 10 ads and 10,000 simulated user rounds, the UCB algorithm learns which ad maximizes clicks by balancing **exploration** (trying less-known ads) with **exploitation** (favoring high-performing ones).

At each round, the algorithm selects the ad with the highest upper confidence bound:

```
UCB(i) = X̄(i) + √( (3/2) · ln(n) / N(i) )
```

- **X̄(i)** — average reward of ad *i* so far
- **n** — current round number
- **N(i)** — number of times ad *i* has been selected

Ads with no selections yet are assigned infinite confidence, ensuring every ad gets tried at least once. Over time, the exploration bonus shrinks and the algorithm converges on the best ad.

## Dataset

`Ads_CTR_Optimisation.csv` — 10,000 rows × 10 columns. Each row is a user round; each column is an ad. Values are binary (1 = click, 0 = no click). The file must be in the same directory as the scripts.

## Dependencies

### Python

```bash
pip install numpy matplotlib pandas
```

### R

No external packages required — uses base R only.

## How to Run

### Python

```bash
python upper_confidence_bound.py
```

### R

```bash
Rscript upper_confidence_bound.R
```

Both scripts output a histogram showing how often each ad was selected. The best-performing ad dominates the distribution.

## Tech Stack

| | Tool | Purpose |
|---|---|---|
| 🐍 | Python 3 | Primary implementation |
| 📊 | NumPy | Numerical operations |
| 📈 | Matplotlib | Histogram visualization |
| 🗂️ | Pandas | CSV data loading |
| 📉 | R | Alternative implementation (base R) |

## Project Structure

```
├── upper_confidence_bound.py   # Python implementation
├── upper_confidence_bound.R    # R implementation
├── Ads_CTR_Optimisation.csv    # Simulated CTR dataset
├── LICENSE                     # MIT License
└── README.md
```

## Known Issues

- The dataset has exactly 10,000 rows. Changing `N` beyond that will cause an index-out-of-bounds error.
- Both scripts expect `Ads_CTR_Optimisation.csv` in the current working directory.
- The simulation uses a fixed dataset rather than a live reward signal — this is a batch replay, not true online learning.

## License

MIT
