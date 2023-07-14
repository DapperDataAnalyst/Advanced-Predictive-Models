import mnist
import numpy as np

# Load the MNIST dataset
x_train, y_train, x_test, y_test = mnist.train_images(), mnist.train_labels(), mnist.test_images(), mnist.test_labels()

# Filter the dataset to include only images of the number 3
filtered_train_images = x_train[y_train == 3]
filtered_train_labels = y_train[y_train == 3]
filtered_test_images = x_test[y_test == 3]
filtered_test_labels = y_test[y_test == 3]


# Q1 ============================================================================================
# Print the shape of the filtered dataset
print("Filtered Train Images Shape:", filtered_train_images.shape)

# Q2 ============================================================================================
max_pixel_value = np.amax(x_train)

# Print the maximum pixel value
print("Maximum pixel value:", max_pixel_value)

# Q3 ============================================================================================
x_three = filtered_train_images

# -*- coding: utf-8 -*-

# Note: This code will not run on its own. This code requires the user to have
#   already loaded the mnist data set and created a subset of the training set
#   of the images corresponding to the digit 3 and stored them in a variable
#   called "x_three"

noise = np.round(np.random.random(list(x_three.shape)) * (x_three.max()+1)) - (x_three.max()+1)/2
dirty_x_three = x_three + noise
dirty_x_three[dirty_x_three > x_three.max()] = x_three.max() # Keep noisy float from going over 255
dirty_x_three[dirty_x_three < x_three.min()] = x_three.min() # Keep noisy float from going under 0

# Reshape the array
reshaped_dirty_x_three = np.reshape(dirty_x_three, (dirty_x_three.shape[0], -1))
print(reshaped_dirty_x_three.shape)

# Q4 ============================================================================================
u, s, vt = np.linalg.svd(reshaped_dirty_x_three)
print(len(s[s > 20_000]))

# Q5 ============================================================================================
print(u.shape)

# Q6 ============================================================================================
x_reconstructed = u[:,0:5] @ np.diag(s[0:5]) @ vt[0:5,:]
print(np.diag(s[0:5]).shape)

