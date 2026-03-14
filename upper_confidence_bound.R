# Upper Confidence Bound

# Importing the dataset (resolve path relative to this script)
script_dir <- tryCatch(
  dirname(sys.frame(1)$ofile),
  error = function(e) getwd()
)
csv_path <- file.path(script_dir, "Ads_CTR_Optimisation.csv")

if (!file.exists(csv_path)) {
  stop(paste("Dataset not found:", csv_path))
}

dataset <- read.csv(csv_path)

# Implementing UCB
N <- nrow(dataset)
d <- ncol(dataset)
ads_selected <- integer(0)
numbers_of_selections <- integer(d)
sums_of_rewards <- integer(d)
total_reward <- 0

for (n in 1:N) {
  ad <- 0
  max_upper_bound <- 0
  for (i in 1:d) {
    if (numbers_of_selections[i] > 0) {
      average_reward <- sums_of_rewards[i] / numbers_of_selections[i]
      delta_i <- sqrt(3/2 * log(n) / numbers_of_selections[i])
      upper_bound <- average_reward + delta_i
    } else {
      upper_bound <- Inf
    }
    if (upper_bound > max_upper_bound) {
      max_upper_bound <- upper_bound
      ad <- i
    }
  }
  ads_selected <- append(ads_selected, ad)
  numbers_of_selections[ad] <- numbers_of_selections[ad] + 1
  reward <- dataset[n, ad]
  sums_of_rewards[ad] <- sums_of_rewards[ad] + reward
  total_reward <- total_reward + reward
}

cat("Total reward:", total_reward, "\n")

# Visualising the results
hist(ads_selected,
     breaks = seq(0.5, d + 0.5, by = 1),
     col = "blue",
     main = "Histogram of ads selections",
     xlab = "Ads",
     ylab = "Number of times each ad was selected",
     xaxt = "n")
axis(1, at = 1:d)
