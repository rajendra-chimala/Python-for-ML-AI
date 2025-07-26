# Blurring
import cv2 as cv

# image = cv.imread("img\image0.jpg")
image = cv.imread("img\image.png")

cv.imshow("image",image)
cv.waitKey(0)

# Average Blurring 

# av_blu = cv.blur(image,(9,9))
   

# cv.imshow("image",av_blu)
# cv.waitKey(0)

# Median Blurring

# Mediab_blu = cv.medianBlur(image,9)

# cv.imshow("image",Mediab_blu)
# cv.waitKey(0)



# Gaussian Blurring


# Gau_blur = cv.GaussianBlur(image,(7,7),9)


# cv.imshow("Gaussian Blurring ",Gau_blur)
# cv.waitKey(0)


# Bilateral Blurring

B_blur = cv.bilateralFilter(image,15,20,20)

cv.imshow("Bilateral Blurring ",B_blur)
cv.waitKey(0)
