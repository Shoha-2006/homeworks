import numpy as np

# 1. Create an array with all zeros, size 10, and set the fifth element to 1
array = np.zeros(10)
array[4] = 1
print(array)

# 2. Create an array with values ranging from 10 to 49
array = np.arange(10, 50)
print(array)

# 3. Reverse the array
reversed_array = array[::-1]
print(reversed_array)

# 4. Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape(3, 3)
print(matrix)

# 5. Find the indices of all non-zero elements in the array [1, 2, 0, 0, 4, 0]
array = np.array([1, 2, 0, 0, 4, 0])
indices = np.nonzero(array)[0]
print(indices)

# 6. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)


# 7. Create a random 3x3 matrix and find the minimum and maximum values
random_matrix = np.random.random((3, 3))
min_val = np.min(random_matrix)
max_val = np.max(random_matrix)
print(random_matrix)
print("Min:", min_val, "Max:", max_val)

# 8. Normalize a 5x5 random matrix so that the values are between 0 and 1
random_matrix = np.random.random((5, 5))
normalized_matrix = (random_matrix - np.min(random_matrix)) / (np.max(random_matrix) - np.min(random_matrix))
print(normalized_matrix)

# 9. Find the closest value in an array to a given number
array = np.array([1, 3, 5, 11, 15, 20, 25])
target = 14
closest_value = array[np.abs(array - target).argmin()]
print(closest_value)

# 10. Replace the maximum element in each row of a 2D array with 0
array = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
for row in array:
    row[np.argmax(row)] = 0
print(array)


# 11. Find the most common value in an array
array = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5])
most_common = np.bincount(array).argmax()
print(most_common)


# 12. Compute the matrix product of a 2D array and its transpose
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
product = np.dot(array, array.T)
print(product)


# 13. Calculate the determinant of a 3x3 matrix
matrix = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
determinant = np.linalg.det(matrix)
print(determinant)


# 14. Find the inverse of a matrix (if it exists)
matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
try:
    inverse_matrix = np.linalg.inv(matrix)
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")
