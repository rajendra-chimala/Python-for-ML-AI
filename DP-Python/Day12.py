import numpy as np

# Array Attributes
# arr = np.array([[1, 2, 3], [4, 7, 6]])

# print("Array:\n", arr)

# # Shape of the array
# print("Shape:", arr.shape)

# # Size of the array
# print("Size of Array : ", arr.size)

# # Dimension of the array
# print("Dimension of Array : ", arr.ndim)

# # Data type of the array
# print("Data type of Array : ", arr.dtype)

# # Size of each element in bytes
# print("Size of each element in bytes:", arr.itemsize)

# # Size of the array in bytes
# print("Total size of the array in bytes:", arr.nbytes)

# Array Accessing 

# arr = np.array([1,2,3,4,5,6])

# # print(arr[0])
# # print(arr)

# print(arr[1:4])  # Slicing from index 1 to 3
# print(arr[1:])   # Slicing from index 1 to the end
# print(arr[:4])   # Slicing from the start to index 3


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Accessing elements in a 2D array
print("Element at (0, 0):", arr[0, 0])

# Accessing a row
print("Row 1:", arr[0])
# Accessing a column
print("Column 1:", arr[:, 0])




