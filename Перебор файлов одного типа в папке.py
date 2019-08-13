import os
dirpath = os.getcwd()
files = os.listdir(dirpath)
images = filter(lambda x: x.endswith('.jpg'), files)
jpg = []
for i in images:
    jpg.append(i)
print(jpg)