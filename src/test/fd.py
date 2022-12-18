
import cv2
import os

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root
HAAR_PATH = os.path.join(ROOT_DIR, "../assets/haarcascade")

# Face
FACE_HAAR = os.path.join(HAAR_PATH, "haarcascade_frontalface_default.xml")

# Load the cascade
face_cascade = cv2.CascadeClassifier(FACE_HAAR)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
width = 320
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

while True:
    # Read the frame
    _, img = cap.read()
    print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # print(faces)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
