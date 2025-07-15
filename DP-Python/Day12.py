import numpy as np 

# arr_3d = np.array([[[2, 3, 5], [6, 8, 9]], [[3, 4, 7], [4, 7, 8]]])
# print(arr_3d)

# 3 x 3 matrix with all elements zero
# zeros_a = np.zeros((3, 3))
# print(zeros_a)

# 3 x 3 matrix with all elements one

# ones_a = np.ones((3,3))
# print(ones_a)

# to create an identity matrix of size 40 x 40
# id_mat = np.eye(40)
# print(id_mat)

# we have to create array of first 50 numbers starting from 1
# arr = np.arange(1, 51, 2)
# print(arr)

# we need an array having 5 values from 1 to 10 evenly spaced
# sp_arr = np.linspace(1, 20, 5)
# print(sp_arr)

# random_arr = np.random.rand(4, 4) # -> this creates a 4 x4 matrix with all values ranging from 0 to 1
# print(random_arr)

# random_arr = np.random.randint(1, 11, size = (4, 4))
# print(random_arr)

# arr = np.array([[10, 20, 30], [30, 40 ,70], [3, 5, 7]], dtype = 'int16')
# print(arr)
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)
# print(arr.itemsize)
# print(arr.nbytes)

# arr_1d = np.array([10, 20, 30, 40, 50])
# print(arr_1d[1:4])

arr_matrix = np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(arr_matrix)
print(arr_matrix[1,:])