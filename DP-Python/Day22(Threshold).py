import cv2 as cv

Image =  cv.imread("img\image.png")

gray = cv.cvtColor(Image,cv.COLOR_BGR2GRAY)


# cv.imshow("Gray",cv.resize(Image,(400,300)))

# Simple Threshold

# threshold, thres_img = cv.threshold(gray,135,255,cv.THRESH_BINARY)
# threshold, thres_img = cv.threshold(gray,135,255,cv.THRESH_BINARY_INV)

# cv.imshow("Threshold",cv.resize(thres_img,(400,300)))
# cv.waitKey(0)




# Adaptive Threshold 

# Adpt_threshold_img = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
# Adpt_threshold_img = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,2)
# Adpt_threshold_img1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,2)


# cv.imshow("Normal",cv.resize(Image,(400,300)))
# cv.imshow("Adaptive Threshold",cv.resize(Adpt_threshold_img,(400,300)))
# cv.imshow("Adaptive Threshold1",cv.resize(Adpt_threshold_img1,(400,300)))


# cv.waitKey(0)


# Color Space 

gray = cv.cvtColor(Image,cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(Image,cv.COLOR_BGR2HSV)
hls = cv.cvtColor(Image,cv.COLOR_BGR2HLS)
ycrcb = cv.cvtColor(Image,cv.COLOR_BGR2YCR_CB)
rgb = cv.cvtColor(Image,cv.COLOR_BGR2RGB)
lab = cv.cvtColor(Image,cv.COLOR_BGR2LAB)


# cv.imshow("Gray Image",cv.resize(gray,(400,300)))
# cv.imshow("HSV Image",cv.resize(hsv,(400,300)))
# cv.imshow("HLS Image",cv.resize(hls,(400,300)))
# cv.imshow("YCR_CB Image",cv.resize(ycrcb,(400,300)))
cv.imshow("RGB Image",cv.resize(rgb,(400,300)))
# cv.imshow("LAB Image",cv.resize(lab,(400,300)))
# cv.imshow("Normal Image",cv.resize(Image,(400,300)))

cv.waitKey(0)


