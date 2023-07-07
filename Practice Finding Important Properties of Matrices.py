import numpy as np

# Q1 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[6,5], [3,4]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Create eigenvector choices from multichoice
# For eigval 9:
goal = np.array([5,3])

test = matrix @ goal == 9 * goal
print(test)

# For eigval 1:
goal = np.array([-1,1])

test = matrix @ goal == 1 * goal
print(test)


# Q2 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[4,-8], [-2,4]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Create eigenvector choices from multichoice
# For eigval 8:
goal = np.array([-2,1])

test = matrix @ goal == 8 * goal
print(test)

# For eigval 0:
goal = np.array([2,1])

test = matrix @ goal == 0 * goal
print(test)


# Q3 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[1,0], [0,1]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Create eigenvector choices from multichoice
# For eigval 1:
goal = np.array([1,0])

test = matrix @ goal == 1 * goal
print(test)

# For eigval 1:
goal = np.array([0,1])

test = matrix @ goal == 1 * goal
print(test)

# For eigval 1:
goal = np.array([1,1])

test = matrix @ goal == 1 * goal
print(test)
