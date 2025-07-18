# Array Reshaping 
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# reshaped_array = arr.reshape(2,5)

# print(reshaped_array)

# auto_reshaped = arr.reshape(5,-1)
# print(auto_reshaped)


# Array Iteration 

# my_array = np.array([1,2,3,4,5,6,7,8,9,10])

# for i in my_array:
#     print(i, end=' ')


# my_Array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for row in my_Array:
#     for element in row:
#         print(element, end=' ')


# Elemet-wise Operations

arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])

print("Addition of Arrays : ", arr_a + arr_b)
print("Subtraction of Arrays : ", arr_a - arr_b)
print("Multiplication of Arrays : ", arr_a * arr_b)
print("Division of Arrays : ", arr_a / arr_b)
print("Element-wise Exponentiation : ", arr_a ** 2)
print("Modulas of Arrays : ", arr_a % 2)



# Universal Functions
print("Square Root of Array : ", np.sqrt(arr_a))
print("Exponential of arr_a : ", np.exp(arr_a))
print("Natural Logarithm : ",np.log(arr_a))
print("Logarithm base 10 : ",np.log10(arr_a))
print("Sin Value : ", np.sign(arr_a))
print("Cos Values : ",np.cos(arr_a))
print("Tan Values : ",np.tan(arr_a))


# Statical Functions

# a = np.array([10, 20, 30, 40, 51])

# mean = np.mean(a)
# print("Mean of the array: ", mean)

# median = np.median(a)
# print("Median of the array: ", median)

# SD = np.std(a)
# print("Standard Deviation of the array: ", SD)

# variance = np.var(a)
# print("Variance of the array: ", variance)

# min = np.min(a)
# print("Minimum value in the array : ", min)

# max = np.max(a)
# print("Maximum value in the array : ", max)

# imin = np.argmin(a)
# print("Index of Minimum value in the array : ", imin)

# imax = np.argmax(a)
# print("Index of Maximum value in the array : ", imax)

##################################################################################
# Matrix Creation

A = np.array([[2,3], [4,5]])
B = np.array([[6,7], [8,9]])
# Matrix Multiplication

# dot_product =  np.dot(A, B) # or A @ B
# print("Dot Product of A and B:\n", dot_product)



# Matrix Transpose

# transposed_A = A.T
# print("Transposed Matrix A:\n", transposed_A)


# # Diterminant of a Matrix
# det_of_A = np.linalg.det(A)
# print("Determinant of Matrix A:", det_of_A)


# # Inverse of a Matrix
# inv_A = np.linalg.inv(A)
# print("Inverse of Matrix A:\n", inv_A)


# # Eiganvalues and Eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(A)
# print("Eigenvalues of Matrix A:", eigenvalues)
# print("Eigenvectors of Matrix A:\n", eigenvectors)


#############################################################################################
# Advacned Mathematical Functions

arr = np.array([1, 2, 3, 4,1,3, 5,2,2])

# Sum of all elements
sum_of_elements = np.sum(arr)
print("Sum of all elements:", sum_of_elements) 

cumulative_sum = np.cumsum(arr)
print("Cumulative Sum of elements:", cumulative_sum)


# Finding Unique Elements

unique = np.unique(arr)
unique,count = np.unique(arr,return_counts=True)
print("Unique elements in the array:", unique)

print("Count of unique elements:", count)


# # Sorting Arrays
# sorted_arr = np.sort(arr)
# asorted_arr = np.argsort(arr)
# print("Sorted Array:", sorted_arr)
# print("Indices of sorted elements:", asorted_arr)



data = np.array([10, 20, 30, 40, 50])
print("25th percentile:", np.percentile(data, 25))
print("50th percentile (median):", np.percentile(data, 50))
print("75th percentile:", np.percentile(data, 75))
