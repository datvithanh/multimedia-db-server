from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
import base64
import io

CLASS_NAMES = ['xoi', 'roll', 'noodles', 'pizza', 'milktea', 'caramen', 'banh_mi', 'birthcake', 'che', 'banh_cuon']

interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

def stringToRGB(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def preprocess_image(image):
    image = image/255
    resized_img = cv2.resize(image, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    batch_inp = np.expand_dims(resized_img, axis=0)
    return batch_inp

def infer(im):
    im = stringToRGB(base64)
    inp = preprocess_image(im).astype(np.float32)

    interpreter.set_tensor(0, inp)
    interpreter.invoke()

    output_data = interpreter.get_tensor(178)
    class_idx = np.argmax(output_data[0])

    if output_data[0][class_idx] < sum(output_data[0])/2:
        return -1
    return CLASS_NAMES[class_idx]

    
