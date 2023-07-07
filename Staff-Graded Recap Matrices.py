import numpy as np
import time

# Q1 ============================================================================================
# Read the CSV file
data = np.genfromtxt('TexasCityDistanceMatrix.csv', delimiter=',')

# Drop the first row and column
matrix = data[1:, 1:]

# Find the maximum value ignoring NaN
max_value = np.nanmax(matrix)
print(max_value)


# Q2 ============================================================================================















