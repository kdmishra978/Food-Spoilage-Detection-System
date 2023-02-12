import numpy as np
from PIL import Image
import os

test_images = []

TEST_DIR = r'D:\Food Spoilage\Main\dataset\test\\'
dirs = ['freshapple', 'freshbanana', 'freshorange', 'rottenapple', 'rottenbanana', 'rottenorange']

fw = open(r'D:\\Food Spoilage\\Main\\Test_Data_new.csv', 'w')
fw.write('FOOD')
fw.write(',')
fw.write('QUALITY')
fw.write('\n')

count = 1

for dir in dirs:
    folder = TEST_DIR + dir + "\\"
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
            test_images.append(data)
            count += 1

fw.close()

test_images = np.array(test_images)