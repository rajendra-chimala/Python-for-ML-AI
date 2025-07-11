# Vector Scaling


# import numpy as np
# A = np.array([[1, 2], [3, 4]])
# x = np.array([5, 6])


# Tx = A @ x
# print(Tx)

# Vector Rotation
# import numpy as np

# theta = np.pi / 4  # 45 degrees
# A = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
# v = np.array([1, 0])
# rotated_v = A @ v
# print("Rotated vector:", rotated_v)


# Reflection 
# import numpy as np

# A = np.array([[1, 0], [0, -1]]) #Reflecting over the x-axis

# v = np.array([3, 4])
# reflected_v = A @ v
# print("Reflected vector:", reflected_v)

# 5 Composition of Linear Transformations
import numpy as np

A = np . array ([[1 , 2] ,
[3 , 4]])

B = np . array ([[0 , 1] ,
[1 , 0]])

x = np . array ([1 , 1])

 # Apply T1 then T2
result = B @ ( A @ x )
print (" Result of T2(T1(x)):", result )

 # Equivalent to (B @ A) @ x
# composed_matrix = B @ A
result2 = (B @ A) @ x
print (" Result using composed matrix :", result2 )