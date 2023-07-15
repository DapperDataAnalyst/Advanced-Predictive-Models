import numpy as np

# Q1 ==================================================================================================
     
# Create a matrix
matrix = np.array([[1,1],
                   [1,1]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Q2 ==================================================================================================
     
# Create a matrix
matrix = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Q3 ==================================================================================================
     
# Create a matrix
matrix = np.full(fill_value=1,
                 shape=(5,5))

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Q4 ==================================================================================================
     
# Create a matrix
matrix = np.array([[1,1,1,0,0],
                  [1,1,1,0,0],
                  [1,1,1,0,0],
                  [0,0,0,1,1],
                  [0,0,0,1,1]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Q5 ==================================================================================================
     
# Create a matrix
matrix = np.array([[1,2],
                   [1,2]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)

# Q6 ==================================================================================================
     
# Create a matrix
matrix = np.array([[1,1,1,0,0],
                  [1,1,1,0,0],
                  [1,1,1,0,0],
                  [0,0,0,1,2],
                  [0,0,0,1,2]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print the eigenvalues
print("Eigenvalues:")
print(eigenvalues)

# Print the eigenvectors
print("\nEigenvectors:")
print(eigenvectors)