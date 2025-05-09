import face_recognition
import numpy as np
from PIL import Image
import io

def get_face_encoding(image_file):
    image = face_recognition.load_image_file(image_file)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        return np.array(encodings[0])
    return None
