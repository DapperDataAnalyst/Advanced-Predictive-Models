library(mvtnorm)
library(ggplot2)

n = 30
mu = 5
sig_sq = 2

# First do independent model
# Generate 30 independent and identically distributed normal random variables
random_variables  <- rnorm(n, mean = mu, sd = sqrt(sig_sq))

# Create a data frame with time points and random variables
time_points <- seq(1, 30)
df <- data.frame(Time = time_points, Random_Variables = random_variables)

# Plot the time series graph
ggplot(data = df, aes(x = Time, y = Random_Variables)) +
  geom_line() +
  geom_point() +
  labs(x = "Time", y = "Random Variables") +
  ggtitle("Time Series Plot of Random Variables with Points")