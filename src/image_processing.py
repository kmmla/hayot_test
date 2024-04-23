import cv2
import numpy as np

def preprocess_images(path1, path2):
    # Preprocessing
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '//haarcascade_frontalface_default.xml')
    
    def detect_and_crop(image):     
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            if len(faces) == 0:
                raise ValueError("No faces found in the image.")
            # Assume the largest detected face is the target face
            x, y, w, h = max(faces, key=lambda item: item[2] * item[3])
            face = gray[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (224, 224))
            return face_resized
    
    try:
        image1 = cv2.imread(path1)
        image2 = cv2.imread(path2)
    
        if image1 is None or image2 is None:
            raise Exception('There is no image available')
        
        face1 = detect_and_crop(image1)
        face2 = detect_and_crop(image2)

        return face1, face2

    except Exception as e:
        print(str(e))
        return None, None

def extract_features(scaled_image1, scaled_image2):
    win_size = (64, 64)
    block_size = (16, 16)
    block_stride = (8, 8)
    cell_size = (8, 8)
    num_bins = 10 

    hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, num_bins)
    try:
        hog_features1 = np.array(hog.compute(scaled_image1))
        hog_features2 = np.array(hog.compute(scaled_image2))
    except Exception as e:
        print(str(e))
        return None, None

    return hog_features1, hog_features2