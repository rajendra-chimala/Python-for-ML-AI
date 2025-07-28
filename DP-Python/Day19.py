# Gradient : Rate of change intensity of pixel in particular direction.
# Edge : Heigh change rate of intensity is called edge.
# Sobel Method : Gradient based method that looks for strong changes int the first derivation. The Sobel edge detector uses a pair of 3 X 3 convolution makes one estimating the gradient in the x-direction and y-direction   

import cv2 as cv
import numpy as np


image = cv.imread("img\image.png")

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)



# cv.imshow("Image",gray)


# Laplacian -> Methos

# lap = cv.Laplacian(gray,cv.CV_64F)
# lap = np.uint8(np.absolute(lap))

# cv.imshow("LAP SHOW",lap)
# cv.waitKey(0)

# Sobel Method

# sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
# sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)

# cv.imshow("Sobel-X",sobel_x)
# cv.imshow("Sobel-Y",sobel_y)
# cv.waitKey(0)


# Canny Method

edge = cv.Canny(gray,threshold1=50,threshold2=100)

cv.imshow("Canny",edge)

cv.waitKey(0)
