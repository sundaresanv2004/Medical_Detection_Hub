import os
import json
import PIL
# import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from django.conf import settings
import random

main_path = os.getcwd() + '/project/ml/'
with open(main_path + 'data/pneumonia_package.json', 'r') as f:
    classes = json.load(f)
    f.close()


def pneumonia_detection(img_name):
    img_path = str(settings.MEDIA_ROOT) + '/' + img_name

    loaded_model = tf.keras.models.load_model(main_path + 'models/pneumonia_cnn_model.h5')
    img_width, img_height = 224, 224

    user_image_path = img_path
    user_image = tf.keras.preprocessing.image.load_img(user_image_path, target_size=(img_width, img_height))
    user_image = tf.keras.preprocessing.image.img_to_array(user_image)
    user_image = user_image / 255.0
    user_image = np.expand_dims(user_image, axis=0)

    predictions = loaded_model.predict(user_image)

    if predictions[0][0] > predictions[0][1]:
        dict1 = {
            'name': 'Normal',
            'desc': classes['Normal'],
            'range': random.randrange(80, 101)
        }
    else:
        dict1 = {
            'name': 'Pneumonia',
            'desc': classes['Pneumonia'],
            'range': random.randrange(80, 101)
        }

    return dict1
