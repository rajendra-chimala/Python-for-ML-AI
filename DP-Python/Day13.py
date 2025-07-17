# Array Reshaping 
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# reshaped_array = arr.reshape(2,5)

# print(reshaped_array)

# auto_reshaped = arr.reshape(5,-1)
# print(auto_reshaped)


# Array Iteration 

my_array = np.array([1,2,3,4,5,6,7,8,9,10])

for i in my_array:
    print(i, end=' ')


# my_Array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# for row in my_Array:
#     for element in row:
#         print(element, end=' ')