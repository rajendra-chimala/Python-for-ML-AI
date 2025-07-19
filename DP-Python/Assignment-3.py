# Assignment 3 Solution 
# Question no 2
# import numpy as np

# def is_linear_transformation(T_matrix, u, v, scalar, tol=1e-8):
    
  
#     def T(x):
#         return T_matrix @ x  
    
#     additivity = np.allclose(T(u + v), T(u) + T(v), atol=tol)

#     homogeneity = np.allclose(T(scalar * u), scalar * T(u), atol=tol)

#     return additivity and homogeneity

# def main():
    
#     T_matrix = np.array([[2, 0], [0, 3]])
    
#     u = np.array([1, 2])
#     v = np.array([3, 4])

#     scalar = 5
    
#     result = is_linear_transformation(T_matrix, u, v, scalar)
#     if (result==True):
#         print("The transformation T is linear.")
#     else:
#         print("The transformation T is not linear.")


# main()


# # Question no 3
# import numpy as np

# # Coefficient matrix A
# A = np.array([
#     [1, 2],
#     [2, 4]
# ])

# # Constant vector b
# b = np.array([
#     [3],
#     [6]
# ])

# Ab = np.array([[1,2,3], [2,4,6]])


# rank_A = np.linalg.matrix_rank(A)
# rank_Ab = np.linalg.matrix_rank(Ab)
# num_vars = A.shape[1]


# if (rank_A == rank_Ab):
#     if (rank_A == num_vars):
#         result = "consistent and independent."
#     else:
#         result = "consistent and cependent"
# else:
#     result = "inconsistent"


# print("Rank of A:", rank_A)
# print("Rank of [A | b]:", rank_Ab)
# print("Result:", result)

# # Question no 4
# import numpy as np


# A = np.array([[2, 3],
#               [5, 4]])
# b = np.array([8, 13])

# # By using np.linalg.solve 
# x_solve = np.linalg.solve(A, b)

# # By using np.linalg.lstsq
# x_lstsq = np.linalg.lstsq(A, b, rcond=None)[0]

# print("Solution using np.linalg.solve:", x_solve)
# print("Solution using np.linalg.lstsq:", x_lstsq)


# QN 5
# import numpy as np

# A = np.array([[1, 2], [3, 4]])
# # Transpose of A
# transposed = A.T
# print("Transpose of A:\n", transposed)

# # Determinant of A
# determinant = np.linalg.det(A)
# print("Determinant of A : \n", determinant)

# # Inverse of A
# inverse = np.linalg.inv(A)
# print("Inverse of A:\n", inverse) 

# # AA-1
# res = A@inverse
# print("Product of A and its inverse:\n", res)


# QN 6

# import numpy as np
# from scipy.linalg import lu

# A = np.array([[2, 3, 1],
#               [4, 7, 7],
#               [6, 18, 22]])

# P, L, U = lu(A)

# print("Matrix A:\n", A)
# print("Permutation matrix P:\n", P)
# print("Lower triangular matrix L:\n", L)
# print("Upper triangular matrix U:\n", U)


# Question no 7
import numpy as np
from scipy.linalg import qr


A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
b = np.array([1, 2, 3])


Q, R = qr(A, mode='economic')

Qt_b = np.dot(Q.T, b)

x = np.linalg.solve(R, Qt_b)

print("Matrix A:\n", A)
print("Vector b:\n", b)
print("Q:\n", Q)
print("R:\n", R)
print("Q^T b:\n", Qt_b)
print("Solution x:\n", x)
