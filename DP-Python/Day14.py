# Revision 
import numpy as np

# Matrix 
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#vector

vect = np.array([1, 2, 3])

# Scaler 

# scalar = 5
# print("Matrix multiplication with scalar:", mat * scalar)

# Transpose of a matrix
# print("Transpose of the matrix:\n", mat.T) 

# # Matrix addition
# mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# mat2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
# mat_sum = mat1 + mat2
# print("Sum of two matrices:\n", mat_sum)

# # Matrix Multiplication
# mat_product = np.dot(mat1, mat2)
# print("Product of two matrices:\n", mat_product)

# # Matrix Inverse 
# inv_mat = np.linalg.inv(mat1)
# print("Inverse of the matrix:\n", inv_mat)


# mat1 = np.array([[1, 2, 3], 
#                 [4, 5, 6],
#                 [7, 8, 9]])

# mat2 = np.array([[5, 7, 8], 
#                 [8, 5, 7],
#                 [7, 3, 4]])

# t_mat1 = mat1.T
# print(t_mat1)

# t_mat2 = mat2.T
# print(t_mat2)

# det1 = np.linalg.det(mat1)
# det2 = np.linalg.det(mat2)
# print(det1)
# print(det2)

# inv_mat2 = np.linalg.inv(mat2)
# print(inv_mat2)


# Task 1
A = np.array([[8, 3,-2], [-4, 7,5],[3,4,-12]])
b = np.array([9, 15, 35])

solution = np.linalg.solve(A, b)
print(solution)