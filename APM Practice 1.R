library(mvtnorm)
library(ggplot2)

n <- 30
mu <- 5
sig_sq <- 2

# First do independent model
# Generate n independent and identically distributed normal random variables
random_variables  <- rnorm(n, mean = mu, sd = sqrt(sig_sq))

# Create a data frame with time points and random variables
time_points <- seq(1, n)
df <- data.frame(Time = time_points, Random_Variables = random_variables)

# Plot the time series graph
ggplot(data = df, aes(x = Time, y = Random_Variables)) +
  geom_line() +
  geom_point() +
  labs(x = "Time", y = "Random Variables") +
  ggtitle("Time Series Plot of Random Variables with Points")

# Now do dependent model
ones_vector <- rep(1, 30)
mu_vector <- runif(1, min=-10, max=10) * ones_vector
rho <- 0.6
sigma_matrix <- matrix(data=rep(0, n*n), nrow=, ncol=n, byrow = TRUE)
for (i in 1:n) {
  for (j in 1:n) {
    covar = sig_sq * rho^abs(i-j)
    sigma_matrix[i,j] <- covar
  }
}

multivar_random_variables <- rmvnorm(n, mu_vector, sigma_matrix)
multivar_df <- data.frame(Time=time_points, Random_Variables=multivar_random_variables[,1])

# Plot the time series graph
ggplot(data = multivar_df, aes(x = Time, y = Random_Variables)) +
  geom_line() +
  geom_point() +
  labs(x = "Time", y = "Multivar Random Variables") +
  ggtitle("Time Series Plot of Random Variables with Points")





