# 🎰 Upper Confidence Bound (UCB)

A clean implementation of the **Upper Confidence Bound** algorithm — a reinforcement learning approach for solving the multi-armed bandit problem. Available in both Python and R.

## What it does

UCB tackles the **exploration vs. exploitation** tradeoff in ad click-through rate (CTR) optimization. Given 10 ads and 10,000 user rounds, the algorithm learns which ad maximizes clicks without wasting too many rounds on underperforming options.

The core idea: pick the ad with the highest upper confidence bound, balancing the observed reward with an exploration bonus that shrinks as an ad gets more selections.

## Tech Stack

| Language | Libraries |
|----------|-----------|
| Python 3 | `numpy`, `matplotlib`, `pandas` |
| R        | Base R (no external packages) |

## Quick Start

### Python

```bash
pip install numpy matplotlib pandas
python upper_confidence_bound.py
```

### R

```bash
Rscript upper_confidence_bound.R
```

Both scripts output a histogram showing how often each ad was selected — you'll see the algorithm converge on the best-performing ad.

## Dataset

`Ads_CTR_Optimisation.csv` — a simulated dataset of 10,000 rounds × 10 ads. Each cell is binary (1 = user clicked, 0 = didn't click). The dataset must be in the same directory as the scripts.

## Project Structure

```
├── upper_confidence_bound.py   # Python implementation
├── upper_confidence_bound.R    # R implementation
├── Ads_CTR_Optimisation.csv    # Simulated ad CTR dataset
├── LICENSE                     # MIT License
└── README.md
```

## License

MIT © [Kaustabh Ganguly](https://github.com/stabgan)
