import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from PIL import Image
import file3
import file6

train_labels = pd.read_csv('./Data_new.csv')['QUALITY']
test_labels = pd.read_csv('./Test_Data_new.csv')['QUALITY']

from kerastuner.tuners import RandomSearch

def build_model(hp):
  model = keras.Sequential()

  model.add(keras.layers.AveragePooling2D(6,3,input_shape=(200,200,3)))

  for i in range(hp.Int("Conv Layers", min_value=0, max_value=3)):
    model.add(keras.layers.Conv2D(hp.Choice(f"layer_{i}_filters", [16,32,64]), 3, activation='relu'))
  
  model.add(keras.layers.MaxPool2D(2,2))
  model.add(keras.layers.Dropout(0.5))
  model.add(keras.layers.Flatten())

  model.add(keras.layers.Dense(hp.Choice("Dense layer", [64, 128, 256, 512, 1024]), activation='relu'))

  model.add(keras.layers.Dense(3, activation='softmax'))

  model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
  
  return model

tuner = RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=32,
)

tuner.search(file3.train_images, train_labels, validation_data=(file6.test_images, test_labels), epochs=10, batch_size=32)

best_model = tuner.get_best_models()[0]

best_model.evaluate(file6.test_images, test_labels)

best_model.save('best_model.model')

# model = keras.Sequential(
#     [keras.layers.AveragePooling2D(6, 3, input_shape=(200, 200, 3)),
#     keras.layers.Conv2D(64, 3, activation='relu'),
#     keras.layers.Conv2D(32, 3, activation='relu'),
#     keras.layers.MaxPool2D(2, 2),
#     keras.layers.Dropout(0.5),
#     keras.layers.Flatten(),
#     keras.layers.Dense(128, activation='relu'),
#     keras.layers.Dense(3, activation='sigmoid')]
# )

# model.compile(optimizer='adam', loss=keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])

# model.fit(file3.train_images, train_labels, epochs=1)

# model.save('food_classification2.model')

# model.evaluate(file6.test_images, test_labels)