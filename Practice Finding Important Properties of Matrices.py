import numpy as np

# Q1
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
goal = np.array([5,3])



