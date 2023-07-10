import numpy as np

# Q1 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[6,5],
                   [3,4]])

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
matrix = np.array([[4,-8],
                   [-2,4]])

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
matrix = np.array([[1,0],
                   [0,1]])

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


# Q4 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[1,0],
                   [0,2]])

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

# For eigval 2:
goal = np.array([0,1])

test = matrix @ goal == 2 * goal
print(test)


# Q5 --------------------------------------------------------------------------------------------------
# Create a matrix
matrix = np.array([[1,0,0],
                   [0,2,0],
                   [0,0,3]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Create eigenvector choices from multichoice
# For eigval 1:
goal = np.array([1,0,0])

test = matrix @ goal == 1 * goal
print(test)

# For eigval 2:
goal = np.array([0,1,0])

test = matrix @ goal == 2 * goal
print(test)

# For eigval 3:
goal = np.array([0,0,1])

test = matrix @ goal == 3 * goal
print(test)


# Q6 --------------------------------------------------------------------------------------------------
seq = range(1,9)
seq = list(seq)
matrix = np.diag(seq)
print(matrix)

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# For eigval 1:
goal = np.array([1,0,0,0,0,0,0,0])

test = matrix @ goal == 1 * goal
print(test)

# For eigval 2:
goal = np.array([0,1,0,0,0,0,0,0])

test = matrix @ goal == 2 * goal
print(test)

# For eigval 8:
goal = np.array([0,0,0,0,0,0,0,1])

test = matrix @ goal == 8 * goal
print(test)


# Q7 --------------------------------------------------------------------------------------------------
matrix = np.array([[1,2],
                   [3,4]])

trace = np.trace(matrix)
print(trace)


# Q8 --------------------------------------------------------------------------------------------------
matrix = np.array([[1,263],
                   [-342,2]])

trace = np.trace(matrix)
print(trace)


# Q9-Q11 --------------------------------------------------------------------------------------------------
matrix = np.array([[-4,0,0,0,0,0],
                   [0,3,0,0,0,0],
                   [0,0,5,0,0,0],
                   [0,0,0,2,0,0],
                   [0,0,0,0,-1,0],
                   [0,0,0,0,0,3]])

# Find the Frobenius norm of the matrix
norm = np.linalg.norm(matrix, ord='fro')
print(norm)

# Find the operator norm of the matrix
norm = np.linalg.norm(matrix, ord=2)
print(norm)

# Find the nuclear norm of the matrix
norm = np.linalg.norm(matrix, ord='nuc')
print(norm)