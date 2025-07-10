import numpy as np

# Defining vector
# v = np.array([1, 2, 3, 4, 5]) 
# print("Vector:\n", v)

# # Matrix Creation

# m = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print("Matrix:\n", m)
# # 3X3 Matrix


# # Scalar Multiplication
# v_scaler = v * 2
# print("Scalar Multiplication:\n", v_scaler)


# B= np.array([[1,2,3],[4,5,6],[7,8,9]])
# C = np.array([[1,3],[3,6]])

# mul = B*C
# print("Matrix Multiplication:\n", mul)



# x = np.array([1,2,3])
# print(type(x))


# Addition of two vectors

# M1 = np.array([[1, 2, 3], [4, 5, 6]])
# M2 = np.array([[7, 8, 9], [10, 11, 12]])

# M3 = M1 + M2
# print("Addition of two matrices:\n", M3)


# Transpose of a matrix

# M1 = np.array([[1, 2, 3], [4, 5, 6]])
# print("Original Matrix:\n", M1)
# M2 = M1.T
# print("Transpose of the Matrix:\n", M2)

# Solve 2x + 3y = 8 and 5x + 4y = 13 using linear algebra using numpy.

# A = np.array([[2,3],[5,4]])
# b = np.array([8,13])

# solution = np.linalg.solve(A,b)

# print("Solution of the equations:\n", solution)







# Answer 

A = np.array([[8,3,-2], [-4,7,5],[3,4,-12]])
b = np.array([9,15,35])
sol =np.linalg.solve(A,b)

print(sol)