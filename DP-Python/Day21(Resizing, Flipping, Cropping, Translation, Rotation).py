# Resizing in Open CV

import cv2 as cv 
import numpy as np


image = cv.imread("img\image.png")



# Resizing 

resized = cv.resize(image,(500,500),interpolation=cv.INTER_CUBIC)

cv.imshow("Image",resized)
cv.waitKey(0)




# Flipping 

flipped = cv.flip(image,-1)
cv.imshow("Flipped",flipped)
cv.waitKey(0)



# Cropping

cropped = image[100:500,200:500]

cv.imshow("Cropped",cropped)

cv.waitKey(0)


# Translation


def translation(img,x,y):
    tran_mat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, tran_mat, dimension)


translated = translation(image, 40, 40)
cv.imshow("Original Image", image)
cv.imshow("Translated Image", translated)

cv.waitKey(0)



# Rotating 


def rotate(img,angle,rotepoint=None):
    (height,width) = img.shape[:2] # 0-> Height 1-> Weight
    
    if(rotepoint is None):
        rotepoint = (width // 2, height // 2)
    
    rotmat = cv.getRotationMatrix2D(rotepoint,angle,1.0)
    dimension = (width,height)
    
    return cv.warpAffine(img,rotmat,dimension)
    


rotated = rotate(image,90)

cv.imshow("Rotated",cv.resize(rotated,(300,200)))
cv.imshow("Normal",cv.resize(image,(300,200)))


cv.waitKey(0)
