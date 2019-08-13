import os
import subprocess
import time

file = input("Введите адрес файла соединения""\n")
dirpath = os.getcwd()

if os.path.exists(file) == True:   #Достаем connection по заданному пути
    print("Путь существует")
    # shutil.copy2(file, dirpath, follow_symlinks=True)
    file = open('%s' % file, 'r')
    text = file.read()
    print(file.read())
    file = open('connection.ini', 'w')
    file.write(text)
    file.close()
    subprocess.Popen("KeyGenerator.exe decrypt connection.ini")
else:
    print("Путь не существует")

while os.path.exists('dconnection.ini') == False:
    time.sleep(1)
final_list = []

with open('dconnection.ini', 'r') as dfile:
    for string in dfile:
        for word in string.split('::'):
            final_list.append(word)
print(final_list)
CONNECTION_STRING = str('pq://' + final_list[3] + ':' + final_list[4] + '@' + final_list[0] + ':' + final_list[1] + '/' + final_list[2])
print(CONNECTION_STRING)
dfile = open('dconnection.ini', 'w')
dfile.write(CONNECTION_STRING)
dfile.close()
