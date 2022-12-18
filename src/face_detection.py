
import cv2
import os
import numpy as np

ROOT_DIR = os.path.dirname(os.path.abspath(
    __file__))  # This is your Project Root
HAAR_PATH = os.path.join(ROOT_DIR, "assets/haarcascade")

# Face
FACE_HAAR = os.path.join(HAAR_PATH, "haarcascade_frontalface_default.xml")


class FaceDetection:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.face_cascade = cv2.CascadeClassifier(FACE_HAAR)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FOURCC,
                     cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def detect(self):
        _, img = self.cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = np.asarray(self.face_cascade.detectMultiScale(gray, 1.1, 4))
        if (faces.size != 0):
            x_cored = faces[0][0]
            print(x_cored)

        return faces

    def release(self):
        self.cap.release()
