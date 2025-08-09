import cv2
import numpy as np
import os  # To navigate folders and files

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to training data folder
dataset_path = "training_images"

# Empty lists to store faces and their corresponding labels
faces = []
labels = []

# Dictionary to map labels to person names (used for display)
label_to_name = {}

# Label counter starting from 0
current_label = 0

# Loop over each folder inside 'training_data'
for person_name in os.listdir(dataset_path):  
    person_folder = os.path.join(dataset_path, person_name)

    # Make sure it's a folder (not a file)
    if not os.path.isdir(person_folder):
        continue

    # Map the current label to the person's name
    label_to_name[current_label] = person_name

    # Loop over images inside that person's folder
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)

        # Read image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            continue  # Skip if image can't be loaded

        # Detect face in the image
        faces_rect = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces_rect:
            # Crop and resize the face
            face_roi = image[y:y+h, x:x+w]
            face_resized = cv2.resize(face_roi, (200, 200))

            # Store the face and its label
            faces.append(face_resized)
            labels.append(current_label)

    current_label += 1  # Move to next label for next person

# Convert lists to numpy arrays
faces = np.array(faces)
labels = np.array(labels)

# Train the recognizer
recognizer.train(faces, labels)
print("✅ Training complete!")

# Load test image
test_img = cv2.imread(r"elon_musk_660_061918012459_100520060232_180620013355_220121094132.jpg")
test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# Detect faces in the test image
test_faces = face_cascade.detectMultiScale(test_gray, scaleFactor=1.1, minNeighbors=5)

# Loop through detected faces
for (x, y, w, h) in test_faces:
    face_roi = test_gray[y:y+h, x:x+w]
    face_resized = cv2.resize(face_roi, (200, 200))

    # Predict the label of the face
    label, confidence = recognizer.predict(face_resized)

    # Map label to person's name
    person_name = label_to_name[label]

    # Draw rectangle and name on the image
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    text = f"{person_name} ({round(confidence, 2)})"
    cv2.putText(test_img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)

# Show result
cv2.imshow("Recognition Result", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
