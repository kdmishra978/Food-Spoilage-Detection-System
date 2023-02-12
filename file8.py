import tensorflow as tf
from tensorflow import keras
import pandas as pd

import file6

model = keras.models.load_model('./best_model.model')

test_labels = pd.read_csv('./Test_Data_new.csv')['QUALITY']

model.evaluate(file6.test_images, test_labels)