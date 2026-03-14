# Upper Confidence Bound (UCB) Algorithm
# Solves the multi-armed bandit problem for ad CTR optimization

import math
import os

import matplotlib.pyplot as plt
import pandas as pd


def main():
    # Importing the dataset (resolve path relative to this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Ads_CTR_Optimisation.csv")

    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"Dataset not found: {csv_path}")

    dataset = pd.read_csv(csv_path)

    # Implementing UCB
    N = len(dataset)
    d = dataset.shape[1]
    ads_selected = []
    numbers_of_selections = [0] * d
    sums_of_rewards = [0] * d
    total_reward = 0

    for n in range(N):
        ad = 0
        max_upper_bound = 0
        for i in range(d):
            if numbers_of_selections[i] > 0:
                average_reward = sums_of_rewards[i] / numbers_of_selections[i]
                delta_i = math.sqrt(3 / 2 * math.log(n + 1) / numbers_of_selections[i])
                upper_bound = average_reward + delta_i
            else:
                upper_bound = math.inf
            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                ad = i
        ads_selected.append(ad)
        numbers_of_selections[ad] += 1
        reward = dataset.to_numpy()[n, ad]
        sums_of_rewards[ad] += reward
        total_reward += reward

    print(f"Total reward: {total_reward}")

    # Visualising the results
    plt.hist(ads_selected, bins=range(d + 1), edgecolor="black", align="left")
    plt.xticks(range(d))
    plt.title("Histogram of ads selections")
    plt.xlabel("Ads")
    plt.ylabel("Number of times each ad was selected")
    plt.show()


if __name__ == "__main__":
    main()
