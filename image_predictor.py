import os
import joblib
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

from __main__ import app

def reshape_and_normalize(data):
    data = np.reshape(data, (28, 28, 1))
    data = np.divide(data, 255)
    data = np.expand_dims(data, axis=0)
    
    return data

def predict(filename):
    # Open the image
    image = load_img(os.path.join(app.config['UPLOAD'], filename), target_size=(28, 28), color_mode="grayscale")
    print("Image opened")
    print(image)

    # Preprocess the image
    #  - convert to numpy array
    #  - reshape and normalize
    img_data = img_to_array(image)
    print(f"Image data shape: {img_data.shape}")
    img_data_tr = reshape_and_normalize(img_data)

    # load model
    model = keras.models.load_model('models/my_model.keras')

    probabilities = model.predict(img_data_tr)

    prediction = np.argmax(probabilities)
    print(f"Predicted digit: {prediction}")
    return prediction