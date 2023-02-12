import os

file_name = 'Data2.csv'

TRAIN_DIR = r'D:\Food Spoilage\Main\dataset\train\\'
dirs = ['freshapple', 'freshbanana', 'freshorange', 'rottenapple', 'rottenbanana', 'rottenorange']

fw = open(file_name, 'w')

fw.write('FOOD')
fw.write(',')
fw.write('QUALITY')
fw.write('\n')
count = 1
for dir in dirs:
    folder = TRAIN_DIR + dir + "\\"
    for filename in os.listdir(folder):
        fw.write('food'+str(count))
        fw.write(',')
        if filename[0] == 'f':
            fw.write('1')
        else:
            fw.write('0')
        fw.write('\n')
        count += 1

fw.close()