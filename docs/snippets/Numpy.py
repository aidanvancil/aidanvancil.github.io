import numpy as np

# Creating NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
arr3 = np.zeros((2, 3))  # Array of zeros
arr4 = np.ones((3, 4))  # Array of ones
arr5 = np.arange(0, 10, 2)  # Array with values from 0 to 10 (exclusive), step 2
arr6 = np.linspace(0, 1, 5)  # Array with five values evenly spaced between 0 and 1
arr7 = np.random.rand(3, 2)  # Array of random values between 0 and 1

# Accessing elements
print(arr1[0])  # Output: 1
print(arr2[1, 2])  # Output: 6

# Array shape and size
print(arr2.shape)  # Output: (2, 3)
print(arr2.size)  # Output: 6

# Array operations
arr8 = arr1 + 5  # Add 5 to each element
arr9 = arr1 * 2  # Multiply each element by 2
arr10 = np.sum(arr2)  # Compute the sum of all elements

# Array slicing
slice1 = arr1[1:4]  # Slice from index 1 to 4 (exclusive)
slice2 = arr2[:, 1]  # Slice all rows, column index 1

# Reshaping arrays
arr11 = arr1.reshape((5, 1))  # Reshape to a column vector
arr12 = arr2.flatten()  # Flatten the array to 1D

# Array broadcasting
arr13 = np.array([1, 2, 3])
arr14 = np.array([[1], [2], [3]])
result = arr13 + arr14  # Broadcasting the addition

# Array aggregation
arr15 = np.array([1, 2, 3, 4, 5])
min_value = np.min(arr15)  # Minimum value
max_value = np.max(arr15)  # Maximum value
mean_value = np.mean(arr15)  # Mean value
sum_value = np.sum(arr15)  # Sum of all elements

# Matrix operations
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
mat3 = np.dot(mat1, mat2)  # Matrix multiplication

# Transposing arrays
transposed = np.transpose(mat1)  # Transpose of the matrix

# Saving and loading arrays
np.save('array.npy', arr1)  # Save array to file
loaded_arr = np.load('array.npy')  # Load array from file
