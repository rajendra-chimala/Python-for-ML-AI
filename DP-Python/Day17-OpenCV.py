import cv2 as cv

# Importing image 

image = cv.imread("./img/fimage.jpg")


# Resizing the image size 
# cv.imshow("Image Show",image)

# resized = cv.resize(image, (500,500))
# cv.imshow("Image Show",resized)
# cv.waitKey(0)


# Flipping 

# flipped = cv.flip(image,-1)
# -1 for both
# 1 for Horizantolly 
# 0 for Vertically
# cv.imshow("Image Show",flipped)
# cv.waitKey(0)


# Converting color in to Gray

# Gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


# cv.imshow("Image Show",Gray)
# cv.waitKey(0)

# cv.rectangle(image,(200,200),(400,400),(0,0,255),5)

# cv.imshow("Image Show",image)
# cv.waitKey(0)

# Edge Detection  

edges = cv.Canny(image,threshold1=100,threshold2=200)


# cv.imshow("Image Show",edges)
# cv.waitKey(0)

# Face Detection project

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# Haar Cascades

face_cascade  = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.03,minNeighbors=15)

for (x,y,w,h) in faces:
    cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),4)

cv.imshow("fd",image)
cv.waitKey(0)



