# Algorithm for skin detection using OpenCV

# Start
# Load the image
# Convert it into the HSV color space
# Define the HSV range for different range of skin colors
# Create the mask using the defined range
# Display the original image and the mask
# Stop 


import numpy as np
import cv2 as cv

image = cv.imread('img/MZ.jpg')

hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)


mask = cv.inRange(hsv_image, lower_skin, upper_skin)

skin = cv.bitwise_and(image,image, mask=mask)

cv.imshow("Skin Detection", cv.resize(skin, (300, 400)))
cv.imshow("Original Image", cv.resize(image, (300, 400)))
cv.imshow("Skin Mask", cv.resize(mask, (300, 400)))
cv.waitKey(0)