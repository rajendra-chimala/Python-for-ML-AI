# Question 1

# import numpy as np


# def Matrix_Multiplication (a,b):
#     return a@b

# def E_wise_multiplication(a,b):
#     return a*b

# def determinant(a):
#     det = np.linalg.det(a)
#     return det
    
# def transpose(a):
#     transposed = a.T
#     return transposed



# def main():
    
#     a = np.array([[2,3],[1,4]])
#     b = np.array([[5,2],[3,1]])
    
    
#     print(f"Matrix Multiplication : ",Matrix_Multiplication(a,b))
#     print(f"Element Wise Matrix Multiplication : ",E_wise_multiplication(a,b))
#     print(f"Determinant : ",determinant(a))
#     print(f"Transposed : ",transpose(a))
    
    
# main()


# Question 2

# import numpy as np

# array = np.random.randint(10,101,(6,6))

# print(f"Random array : {array}")

# diagonal_elemtnts = np.diag(array)

# print(f"Diagonal elements of an array : {diagonal_elemtnts}")


# new_matrix = array.astype(float)

# even_pos = (new_matrix %2 == 0)

# new_matrix[even_pos] = np.sqrt(new_matrix[even_pos])

# print(f"The Replaced Matrix with even number with squar root : {new_matrix}")

# print(f"Mean value : {np.mean(new_matrix)}")
# print(f"Median value : {np.median(new_matrix)}")
# print(f"Standard Deviation value : {np.std(new_matrix)}")


# reshaped_array = new_matrix.reshape(4,9)


# print(f"REshaped Matris is : {reshaped_array}")


# Question 3

# import cv2 as cv

# image = cv.imread("img\image.png")

# gray_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# cv.imshow("Gray Image",gray_img)
# cv.imshow("Original Image",image)

# cv.waitKey(0)
# cv.destroyAllWindows()


# cv.imwrite("img\copy_img.png",gray_img)


# print(f"Image Height : ",image.shape[0])
# print(f"Image Weight : ",image.shape[1])
# print(f"Image Channel : ",image.shape[2])
