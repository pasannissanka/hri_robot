
import cv2
import os
import numpy as np

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
    img_size = img.shape

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = np.asarray(face_cascade.detectMultiScale(gray, 1.1, 4))
    region_x = 0
    region_y = 0
    if (faces.size != 0):
        print(img_size)
        region_bnd_x = img_size[0]/3
        region_bnd_y = img_size[1]/3
        x_cored = faces[0][0]
        y_cored = faces[0][1]
        if 0 < x_cored < region_bnd_x:
            region_x = 1
        elif region_bnd_x < x_cored < region_bnd_x * 2:
            region_x = 2
        elif region_bnd_x * 2 < x_cored < region_bnd_x * 3:
            region_x = 3
        if 0 < y_cored < region_bnd_y:
            region_y = 1
        elif region_bnd_y < y_cored < region_bnd_y * 2:
            region_y = 2
        elif region_bnd_y * 2 < y_cored < region_bnd_y * 3:
            region_y = 3
    print(faces, (region_x, region_y))

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
