from PIL import Image
import os

TRAIN_DIR = r'D:\Food Spoilage\Main\dataset\train\\'
TEST_DIR = r'D:\Food Spoilage\Main\dataset\test\\'

dirs = ['freshapple', 'freshbanana', 'freshorange', 'rottenapple', 'rottenbanana', 'rottenorange']

for dir in dirs:
    folder = TEST_DIR + dir + "\\"
    
    for file_name in os.listdir(folder):
        source = folder + file_name
        im = Image.open(source)
        im = im.resize((200,200))
        im.save(fp=source)