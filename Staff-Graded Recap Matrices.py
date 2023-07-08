import numpy as np
from scipy.sparse import csr_matrix
import time

# Part (a) ============================================================================================
# Read the CSV file
data = np.genfromtxt('TexasCityDistanceMatrix.csv', delimiter=',')

# Drop the first row and column
matrix = data[1:, 1:]

# Find the maximum value ignoring NaN
max_value = np.nanmax(matrix)
print(max_value)


# Part (b) ============================================================================================
# Note that the row and column headers have been removed, and thus Katy is the 750th row in the matrix
# in its current form

# Find row of interest
row_values = matrix[749, :]

# Remove zeroes
nonzero_values = row_values[row_values != 0]

# Find mins
min_nonzeroes = np.nanmin(nonzero_values)
print(min_nonzeroes)


# Find locations within 25 miles of Flower Mound
# Flower Mound is the 507th row in the matrix
# Find row of interest
row_values = matrix[506, :]

# Remove zeroes
nonzero_values = row_values[row_values != 0]

# Find values less than 25
values = nonzero_values[nonzero_values <= 25]
print(len(values))


# Part (c) ============================================================================================
start = time.time()
np.sum(matrix)
end = time.time()
print(end - start)


# Part (d) ============================================================================================
# Set values greater than 50 to zero
mod_matrix = matrix
mod_matrix[mod_matrix > 50] = 0

# Set NAs to zero
mod_matrix = np.nan_to_num(mod_matrix)

start = time.time()
np.sum(mod_matrix)
end = time.time()
print(end - start)


# Part (e) ============================================================================================
sparse_matrix = csr_matrix(matrix)

start = time.time()
np.sum(sparse_matrix)
end = time.time()
print(end - start)








