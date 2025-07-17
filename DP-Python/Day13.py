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

# print("Addition of Arrays : ", arr_a + arr_b)
# print("Subtraction of Arrays : ", arr_a - arr_b)
# print("Multiplication of Arrays : ", arr_a * arr_b)
# print("Division of Arrays : ", arr_a / arr_b)
# print("Element-wise Exponentiation : ", arr_a ** 2)
# print("Modulas of Arrays : ", arr_a % 2)



# Universal Functions
# print("Square Root of Array : ", np.sqrt(arr_a))
# print("Exponential of arr_a : ", np.exp(arr_a))
# print("Natural Logarithm : ",np.log(arr_a))
# print("Logarithm base 10 : ",np.log10(arr_a))
# print("Sin Value : ", np.sign(arr_a))
# print("Cos Values : ",np.cos(arr_a))
# print("Tan Values : ",np.tan(arr_a))


# Statical Functions

a = np.array([10, 20, 30, 40, 51])

mean = np.mean(a)
print("Mean of the array: ", mean)

median = np.median(a)
print("Median of the array: ", median)

SD = np.std(a)
print("Standard Deviation of the array: ", SD)

variance = np.var(a)
print("Variance of the array: ", variance)

min = np.min(a)
print("Minimum value in the array : ", min)

max = np.max(a)
print("Maximum value in the array : ", max)

imin = np.argmin(a)
print("Index of Minimum value in the array : ", imin)

imax = np.argmax(a)
print("Index of Maximum value in the array : ", imax)