import os
import json
import PIL
# import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from django.conf import settings
import random

main_path = os.getcwd() + '/home/ml/'
with open(main_path + 'data/skin_package.json', 'r') as f:
    classes = json.load(f)
    f.close()


def skin_cancer_cla(img_name):
    img_path = str(settings.MEDIA_ROOT) + '/' + img_name
    image = PIL.Image.open(img_path)
    image = image.resize((28, 28))
    model = tf.keras.models.load_model(main_path + 'models/Skin_Cancer.h5')

    # img = np.array(image)
    # img = img.reshape(-1, 28, 28, 3)
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()

    img = np.array(image).reshape(-1, 28, 28, 3)

    result = model.predict(img)
    result = result.tolist()
    max_prob = max(result[0])
    class_ind = result[0].index(max_prob)
    cls = classes.get(str(class_ind), None)
    dict1 = {
        'name': cls['full_name'],
        'desc': cls['description'],
        'range': random.randrange(80, 101)
    }

    return dict1
