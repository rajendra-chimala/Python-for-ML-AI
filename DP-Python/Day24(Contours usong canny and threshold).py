# Contours using threshold and Canny 



import cv2 as cv

# Load image
image = cv.imread("img/image.png")

# Convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred_img = cv.GaussianBlur(gray, (5, 5), 0)

# Canny Edge Detection
edge = cv.Canny(blurred_img, 100, 200)

# Find Contours from Canny
contours_canny, _ = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count = len(contours_canny)

# Thresholding
_, thres_img = cv.threshold(blurred_img, 120, 220, cv.THRESH_BINARY)

# Find Contours from Threshold
contours_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(contours_thres)

# Print contour counts
print("Canny Contours:", count)
print("Threshold Contours:", count2)

# Draw contours
img_thres = image.copy()
img_canny = image.copy()

cv.drawContours(img_canny, contours_canny, -1, (0, 255, 0), 2)
cv.drawContours(img_thres, contours_thres, -1, (0, 0, 255), 2)

# Show images
cv.imshow("Canny Contours", img_canny)
cv.imshow("Threshold Contours", img_thres)

cv.waitKey(0)
cv.destroyAllWindows()
