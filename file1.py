import os

TRAIN_DIR = r'D:\Food Spoilage\Main\dataset\train\\'
TEST_DIR = r'D:\Food Spoilage\Main\dataset\test\\'

dirs = ['freshapple', 'freshbanana', 'freshorange', 'rottenapple', 'rottenbanana', 'rottenorange']

for dir in dirs:
    count = 1
    folder = TEST_DIR + dir + "\\"
    
    for file_name in os.listdir(folder):
        source = folder + file_name

        destination = folder + dir + str(count) + ".png"

        if not os.path.isfile(destination):
            os.rename(source, destination)
        count += 1