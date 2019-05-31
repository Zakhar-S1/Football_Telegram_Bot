import cv2, os
import numpy as np
from PIL import Image

def recognize_teacher(image):

    cascadePath = "./haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)
    recognizer = cv2.face.LBPHFaceRecognizer_create(1,8,8,8,123)
    recognizer.read('/Users/user/Desktop/telegram-env/telegram-bot/model.xml')

    gray = Image.open(image).convert('L')
    image = np.array(gray, 'uint8')
    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    number = 0
    conf = 0

    for (x, y, w, h) in faces:
        number, conf = recognizer.predict(image[y: y + h, x: x + w])

    return number, conf
