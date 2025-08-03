# Bitwise Operator in Open CV
import cv2 as cv
import numpy as np

# Creating Image

img1 = np.zeros((300,300),dtype="uint8")
img2 = np.zeros((300,300),dtype="uint8")

# Draw White Rectangle 
cv.rectangle(img1,(50,50),(250,250),255,-1)

# Draw White Circle
cv.circle(img2,(150,150),120,255,-1)


cv.imshow("Rectangle",img1)
cv.imshow("Circle",img2)


# AND Opetarion

bit_and = cv.bitwise_and(img2,img1)
cv.imshow("Bit AND",bit_and)


# OR Operation

bit_or = cv.bitwise_or(img1,img2)
cv.imshow("OR",bit_or)

# XOR Operation 

bit_xor = cv.bitwise_xor(img1,img2)
cv.imshow("XOR",bit_xor)

# NOT Opetarion 
bit_not = cv.bitwise_not(img2)
cv.imshow("NOT",bit_not)



cv.waitKey(0)
cv.destroyAllWindows()