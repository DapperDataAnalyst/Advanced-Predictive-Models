# Set values
sigma2 <- 10
l <- 1
si <- c(0.6, 0.2, 0.3, 0.9)
sj <- c(0.6, 0.2, 0.3, 0.9)
cov_matrix <- matrix(0, nrow = 4, ncol = 4)

# Fill out covariance matrix
for (i in 1:length(si)){
  for(j in 1:length(sj)){
    sqr_expo <- sigma2*exp(-(abs(si[i] - sj[j]) * l)^2)
    
    cov_matrix[i,j] <- sqr_expo
  }
}

# Find conditional mean and variance
sigma12 <- cov_matrix[1, 2:4]
sigma22 <- cov_matrix[2:4, 2:4]
sigma21 <- cov_matrix[2:4,1]
condit_mean <- c(3,4,-1)%*%solve(sigma22)%*%sigma12

condit_var <- cov_matrix[1,1] - sigma12%*%solve(sigma22)%*%sigma21
condit_sd <- sqrt(condit_var)


# Now with nugget
sigma_e2 <- 0.01
for (i in 1:length(si)){
  for(j in 1:length(sj)){
    sqr_expo <- sigma2*exp(-(abs(si[i] - sj[j]) * l)^2) + sigma_e2*ifelse(i==j,1,0)
    
    cov_matrix[i,j] <- sqr_expo
  }
}

sigma12 <- cov_matrix[1, 2:4]
sigma22 <- cov_matrix[2:4, 2:4]
sigma21 <- cov_matrix[2:4,1]
condit_mean <- c(3,4,-1)%*%solve(sigma22)%*%sigma12

condit_var <- cov_matrix[1,1] - sigma12%*%solve(sigma22)%*%sigma21
condit_sd <- sqrt(condit_var)
