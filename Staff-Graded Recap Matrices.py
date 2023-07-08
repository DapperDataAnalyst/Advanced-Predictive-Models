import numpy as np
from scipy.sparse import csr_matrix
import time
import pandas as pd

# Part (a) ============================================================================================
# Read the CSV file
data = np.genfromtxt('TexasCityDistanceMatrix.csv', delimiter=',')
key = pd.read_csv('TexasCityKey.csv', encoding = "ISO-8859-1")

# Drop the first row and column
matrix = data[1:, 1:]

# Find the maximum value ignoring NaN
max_value = np.nanmax(matrix)
print(max_value)


# Part (b) ============================================================================================
# Note that the row and column headers have been removed, and thus Katy is the 750th row in the matrix
# in its current form

# Specify the row index
row_index = 749

# Find the column index of the lowest non-zero value that is not NaN in the specified row
row_values = matrix[row_index]
nonzero_indices = np.where((row_values != 0) & (~np.isnan(row_values)))[0]

min_index = np.argmin(row_values[nonzero_indices])
column_index = nonzero_indices[min_index]

print(f"Column index of the lowest non-zero value in row {row_index} is {column_index}")
print(key.iloc[column_index,1])


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

