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
# import numpy as np
# from scipy.linalg import qr


# A = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])
# b = np.array([1, 2, 3])


# Q, R = qr(A, mode='economic')

# Qt_b = np.dot(Q.T, b)

# x = np.linalg.solve(R, Qt_b)

# print("Matrix A:\n", A)
# print("Vector b:\n", b)
# print("Q:\n", Q)
# print("R:\n", R)
# print("Q^T b:\n", Qt_b)
# print("Solution x:\n", x)


# QN 20

# import numpy as np

# def get_column_basis_numpy(A, tol=1e-10):
   
#     A = np.array(A, dtype=float)
#     Q, R = np.linalg.qr(A)
#     diag = np.abs(np.diag(R))
    
    
#     independent_indices = [i for i, val in enumerate(diag) if val > tol]
#     basis_columns = [A[:, i] for i in independent_indices]
    
#     return basis_columns, independent_indices


# def main():
#     A = np.array([
#         [1, 2, 3],
#         [2, 4, 6],
#         [3, 6, 9]
#     ])

#     basis, indices = get_column_basis_numpy(A)

#     print("Indices of linearly independent columns:", indices)
#     print("Basis for the column space:")
#     for col in basis:
#         print(col)
        
        
# main()

# import numpy as np
# import matplotlib.pyplot as plt

# A1 = np.array([[1, 1],
#                [1, -1]])
# b1 = np.array([2, 0])

# x1 = np.linalg.solve(A1, b1)

# x_vals = np.linspace(-2, 4, 100)
# y1 = 2 - x_vals      
# y2 = x_vals          

# plt.figure(figsize=(6, 5))
# plt.plot(x_vals, y1, label='x + y = 2')
# plt.plot(x_vals, y2, label='x - y = 0')
# plt.plot(x1[0], x1[1], 'ro', label=f'Solution ({x1[0]}, {x1[1]})')
# plt.title('Consistent System: Unique Solution')
# plt.xlabel('x'); plt.ylabel('y')
# plt.axhline(0, color='gray', linewidth=0.5)
# plt.axvline(0, color='gray', linewidth=0.5)
# plt.legend()
# plt.grid(True)
# plt.show()



# Question No 9
# import numpy as np

# A = np.array([[2, 4],
#               [1, 2]])

# b = np.array([6, 3])

# det_A = np.linalg.det(A)
# print("Determinant of A:", det_A)

# if det_A == 0:
#     print("Matrix A is not invertible (singular).")
# else:
#     x = np.linalg.inv(A) @ b
#     print("Solution:", x)

# try:
#     x = np.linalg.solve(A, b)
#     print("Solution:", x)
# except np.linalg.LinAlgError as e:
#     print("Cannot solve the system:", e)

# Question No 10
# import numpy as np

# def classify_linear_system(A, b):
#     A = np.array(A, dtype=float)
#     b = np.array(b, dtype=float).reshape(-1, 1) 

#     augmented = np.hstack((A, b))

#     rank_A = np.linalg.matrix_rank(A)
#     rank_aug = np.linalg.matrix_rank(augmented)
#     num_vars = A.shape[1]

#     if rank_A == rank_aug:
#         if rank_A == num_vars:
#             return "unique solution"
#         else:
#             return "infinite solutions"
#     else:
#         return "Inconsistent."

# A1 = [[2, 1],
#       [1, -1]]
# b1 = [4, 1]
# print("Result : ", classify_linear_system(A1, b1))  


# Question 13

# import numpy as np

# v1 = [1, 0, 0]
# v2 = [0, 1, 0]
# v3 = [0, 0, 1]

# A = np.column_stack((v1, v2, v3))


# rank = np.linalg.matrix_rank(A)

# print("Matrix formed by vectors:\n", A)
# print("Rank of the matrix:", rank)

# if rank == 3:
#     print("The vectors form a basis for R^3 (they are linearly independent and span the space).")
# else:
#     print("The vectors do NOT form a basis for R^3.")

# Qn 14

    # import numpy as np

    # A = np.array([
    #     [1, 2, 3],
    #     [2, 4, 6],
    #     [1, 1, 1]
    # ])

    # rank = np.linalg.matrix_rank(A)
    # print("Rank of A:", rank)
    
    
# import numpy as np
# from sympy import Matrix

# A = np.array([
#     [1, 2, 3],
#     [2, 4, 6],
#     [1, 1, 1]
# ])

# rank_numpy = np.linalg.matrix_rank(A)

# A_sym = Matrix(A)
# ref, _ = A_sym.rref() 

# pivot_columns = _.tolist()
# pivot_count = len(pivot_columns)

# print("Row Echelon Form (RREF):")
# print(ref)
# print("Pivot Columns:", pivot_columns)
# print("Number of Pivot Columns:", pivot_count)
# print("Rank from NumPy:", rank_numpy)





# import numpy as np


# u = np.array([1, 2, 3])      
# v = np.array([4, 5, 6])      


# A = np.outer(u, v)

# rank = np.linalg.matrix_rank(A)

# _, s, _ = np.linalg.svd(A)
# independent_columns = np.sum(s > 1e-10)

# print("Matrix A:\n", A)
# print("Rank of A:", rank)
# print("Number of Linearly Independent Columns:", independent_columns)


# import numpy as np

# def full_rank_percentage(n=10, size=4):
#     full_rank_count = 0

#     for i in range(n):
#         A = np.random.randint(-10, 10, (size, size)) 
#         rank = np.linalg.matrix_rank(A)
#         print(f"Matrix {i+1}:\n{A}\nRank: {rank}\n")
#         if rank == size:
#             full_rank_count += 1

#     percentage = (full_rank_count / n) * 100
#     print(f"Full-rank matrices: {full_rank_count} out of {n}")
#     print(f"Percentage of full-rank matrices: {percentage:.2f}%")
#     return percentage


# full_rank_percentage()


import numpy as np

A = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 1]
], dtype=float)

rank = np.linalg.matrix_rank(A)
print("Rank of A:", rank)


u, s, vh = np.linalg.svd(A)
tolerance = 1e-10
independent_indices = np.where(s > tolerance)[0]

basis_columns = A[:, independent_indices]

print("Basis columns (from original A):")
print(basis_columns)


