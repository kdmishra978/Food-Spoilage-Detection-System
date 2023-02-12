import numpy as np
from PIL import Image
import os

train_images = []

TRAIN_DIR = r'D:\Food Spoilage\Main\dataset\train\\'
dirs = ['freshapple', 'freshbanana', 'freshorange', 'rottenapple', 'rottenbanana', 'rottenorange']

fw = open(r'D:\\Food Spoilage\\Main\\Data_new.csv', 'w')
fw.write('FOOD')
fw.write(',')
fw.write('QUALITY')
fw.write('\n')

count = 1

for dir in dirs:
    folder = TRAIN_DIR + dir + "\\"
    for filename in os.listdir(folder):
        image = Image.open(folder+filename)
        data = np.asarray(image)
        
        if data.shape == (200, 200, 3):
            fw.write('food'+str(count))
            fw.write(',')
            if filename[0] == 'f':
                fw.write('1')
            else:
                fw.write('0')
            fw.write('\n')
            data = data/255
            train_images.append(data)
            count += 1

fw.close()

train_images = np.array(train_images)