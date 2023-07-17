import numpy as np
import matplotlib.pyplot as plt

# Get data
data = np.genfromtxt('PCAData.csv', delimiter=',')
print(data)
print(data[:,1:3])