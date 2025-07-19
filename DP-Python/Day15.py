# Broadcasting
import numpy as np
'''
# Scaler to Vector broadcasting 

arr = np.array([1,2,3,4,5,6])
# scaler = 5

newArr = arr*scaler

print("Array : \n",arr)
print("New Array : \n",newArr)


Broadcasting with Matrix

mat = np.array([[1,2,3],[2,3,4],[3,4,5]])
scaler = 2
vect = np.array([1,2,3])

fmat = mat*scaler 
fmat = mat*vect
print("Matrix : ",mat)
print("Matrix after Broadcasting : ",fmat)


# Sorting Row wise and column wise using the axis 0 and axis 1

m = np.array([[1,2,3,4],[4,2,3,1]])

sm = np.sort(m, axis=1) For row wise sorting 
sm = np.sort(m, axis=0) #column wise sorting 

print(sm)

'''

# Matrix Appending

original_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
new_row = np.array([[3,2,1]])
new_column = np.array([[9],[9],[9]])


# new_matrix = np.append(original_matrix,new_column,axis=0)
new_matrix = np.append(original_matrix,new_column,axis=1)
print("Original Matrix  :\n",original_matrix)
print("New Matrix  :\n",new_matrix)