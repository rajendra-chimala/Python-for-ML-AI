# Bitwise Operator in Open CV
import cv2 as cv
import numpy as np

# Creating Image

# img1 = np.zeros((300,300),dtype="uint8")
# img2 = np.zeros((300,300),dtype="uint8")

# Draw White Rectangle 
# cv.rectangle(img1,(50,50),(250,250),255,-1)

# Draw White Circle
# cv.circle(img2,(150,150),120,255,-1)


# cv.imshow("Rectangle",img1)
# cv.imshow("Circle",img2)


# # AND Opetarion

# bit_and = cv.bitwise_and(img2,img1)
# cv.imshow("Bit AND",bit_and)


# # OR Operation

# bit_or = cv.bitwise_or(img1,img2)
# cv.imshow("OR",bit_or)

# # XOR Operation 

# bit_xor = cv.bitwise_xor(img1,img2)
# cv.imshow("XOR",bit_xor)

# # NOT Opetarion 
# bit_not = cv.bitwise_not(img2)
# cv.imshow("NOT",bit_not)

# Masking


image = cv.imread("img\image0.jpg")
cv.imshow("Image",image)



# # Create mask
# img_mask = np.zeros(image.shape[:2],dtype="uint8")

# # Create Circle

# cv.circle(img_mask,(250,250),170,255,-1)



# # Apply the Mask
# masked_image = cv.bitwise_and(image,image,mask = img_mask)

# cv.imshow("Masked Image",masked_image)
# cv.imshow("Mask",img_mask)


# cv.waitKey(0)
# cv.destroyAllWindows()



# Color Channel


# Splitting color channels 


B,G,R = cv.split(image)


# cv.imshow("Blue",B)
# cv.imshow("Green",G)
# cv.imshow("Red",R)


Merged = cv.merge([B,G,R])


cv.imshow("Merged",Merged)


# print(Merged.shape,image.shape)


zeros = np.zeros_like(B)
# Merge to create true-color visualizations
blue_visual = cv.merge([B, zeros, zeros])
green_visual = cv.merge([zeros, G, zeros])
red_visual = cv.merge([zeros, zeros, R])


cv.imshow('True Blue', blue_visual)
cv.imshow('True Green', green_visual)
cv.imshow('True Red', red_visual)



    
cv.waitKey(0)
cv.destroyAllWindows()