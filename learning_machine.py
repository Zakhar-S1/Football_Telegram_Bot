import cv2, os
import numpy as np
from PIL import Image
from config import dictionary

cascadePath = "./haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)

recognizer = cv2.face.LBPHFaceRecognizer_create(1,8,8,8,123) #шаблоны

def get_images(path):

    image_paths = [os.path.join(path, f) for f in os.listdir(path)  if f.endswith('.jpg')]

    images = []
    labels = []

    for image_path in image_paths:

        gray = Image.open(image_path).convert('L')
        image = np.array(gray, 'uint8')

        teacher_id = dictionary.get(image_path[61:-4])

        faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(teacher_id)

            cv2.imshow("", image[y: y + h, x: x + w])
            cv2.waitKey(50)

    return images, labels

if __name__ == '__main__':

    path = '/Users/user/Desktop/telegram-env/telegram-bot/Football_Faces'

    images, labels = get_images(path)
    cv2.destroyAllWindows()

    recognizer.train(images, np.array(labels))
    recognizer.save('/Users/user/Desktop/telegram-env/telegram-bot/model.xml')

    print("Trained")
