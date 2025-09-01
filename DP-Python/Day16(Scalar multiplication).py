import numpy as np
from sklearn.decomposition import PCA
v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

# sum = v1 +v2 

# print(f"The sum of vector is {sum}")

# # Scaler multiplication 

# scaler = 5

# SM = v1*scaler

# print(f"The sum of vector multiplication is {SM}")


# Norm in Linear Algebra 

# value = np.dot(v1,v2)

# print(value)


# V = np.array([1,20,40,30,50,60,100])

# n_v = np.linalg.norm(V)

# print(f"The norm value is : {n_v}")

# a = np.array([1,2,3,4,5])
# b = np.array([10,2,-3,4,5])

# proj = (np.dot(a,b)/np.dot(b,b))*b

# print(f"The Projection of a and b is : {proj}")


# Linear combination 

# M = np.array([[1,2,3],[3,2,1]])

# c1, c2 = 1.5,3

# lc = c1 * M[0] + c2 * M[1]

# print(f"The Linear combination is {lc}")

# 

# M = np.stack([v1,v2], axis=1)

# rank = np.linalg.matrix_rank(M)


# is_independent = (rank == M.shape[1])

# if is_independent:
#     print("The vector is in dependent !")
# else:
#     print("The vector is dependent !")

# Dimension Reduction using PCA

X = np.random.rand(5,4)

p = PCA(n_components=3)

x_pca = p.fit_transform(X)

print(X)
print(x_pca)

