import cv2

import base64
import io
from imageio import imread
import numpy as np

from sagemaker.tensorflow import TensorFlowPredictor

# classifier_path = "lambda_function/haarcascade_frontalface_default.xml"
classifier_path = "haarcascade_frontalface_default.xml"
print(classifier_path)

emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
face_classifier_frontal = cv2.CascadeClassifier(classifier_path)
print("classifier created")

emotion_model = TensorFlowPredictor('smileDemoTesorflow')



# event: {query: "query"}
def handler(event, context):
    b64_string = event['body']
    prediction = process_image(b64_string)
    print("here")
    print(prediction)
    result = False
    if "happy" in prediction:
        result = True
        
    return {
        'statusCode': 200,
        'body': result
    }
    
 


def process_image(b64_string) -> list: 
    
    convertedbytes = base64.b64decode(b64_string)
    img = imread(io.BytesIO(base64.b64decode(convertedbytes)))
    image_cv2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
    faces_frontal = face_classifier_frontal.detectMultiScale(image_cv2)
    print(faces_frontal)

    emotions = []
    
    for (x, y, w, h) in faces_frontal:    
        # (x, y, w, h) = faces_frontal[0]
        face_roi = image_cv2[y:y + h, x:x + w]
        resized_face = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)
        normalized_face = resized_face / 255.0
        reshaped_face = normalized_face.reshape(1, 48, 48, 1)
        # preds = emotion_model.predict(reshaped_face)[0]
        response = emotion_model.predict(reshaped_face)
        predictions = response['predictions']
        print(predictions)
        emotion_idx = np.array(predictions[0]).argmax()
        # emotion_idx = preds.argmax()
        emotion = emotion_labels[emotion_idx]
        print(emotion)
        emotions.append(emotion)

    # if emotion != "happy":
    #     return False

    return emotions