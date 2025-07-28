import cv2 as cv

# cap = cv.VideoCapture(0)

# while True:
#     set_f,frame = cap.read()
#     cv.imshow("Face",frame)
    
#     if cv.waitKey(1) & 0xFF ==ord('q'):
#         break



# Video face detection 

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)


while True :
    tr,frame = cap.read()
    
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5) #X Y W H
    
    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        cv.imshow("Face Detection",frame)
        
    if cv.waitKey(1) & 0xFF == ord(" "):
        break
        
cap.release()
cv.destroyAllWindows()
    
    