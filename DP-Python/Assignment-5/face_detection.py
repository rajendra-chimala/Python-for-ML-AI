import cv2
import numpy as np
import os


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"
faces, labels = [], []
label_to_name = {}
label_count = 0

for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)
    if not os.path.isdir(person_path):
        continue

    label_to_name[label_count] = person_name
    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces_detected:
            face_resized = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            faces.append(face_resized)
            labels.append(label_count)
    label_count += 1

faces = np.array(faces, dtype=np.uint8)
labels = np.array(labels, dtype=np.int32)

recognizer.train(faces, labels)

cap = cv2.VideoCapture(0)
AUTHORIZED_PERSON = "Rajendra Chimala"
CONFIDENCE_THRESHOLD = 75  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_detected = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces_detected:
        face_resized = cv2.resize(gray_frame[y:y+h, x:x+w], (200, 200))
        label, confidence = recognizer.predict(face_resized)
        name = label_to_name.get(label, "Unknown")

        if confidence < CONFIDENCE_THRESHOLD:
            color = (0, 255, 0)  # Green
            if name == AUTHORIZED_PERSON:
                print("Access Granted")
        else:
            color = (0, 0, 255)  # Red

        if confidence <60:
            cv2.putText(frame, f"[{name} ({int(confidence)})]", (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    cv2.imshow("Face Recognition", cv2.resize(frame,(400,400)))

    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
