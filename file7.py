import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img_width = 200
img_height = 200

img = keras.preprocessing.image.load_img('./t8.png', target_size=(img_width, img_height))
x = keras.preprocessing.image.img_to_array(img)
x = np.expand_dims(x, axis=0)

print(x.shape)

model = keras.models.load_model('./best_model.model')

images = np.vstack([x])

classes = model.predict(images, batch_size=32)
if int(classes[0][0]) == 1:
    print("rotten")
else:
    print("fresh")
