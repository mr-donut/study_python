#Скачать текстовой файл с заданного адреса и подсчитать в нем количество строк

import requests
r = requests.get(input())
r = (r.text.strip(' ').splitlines())
a = 0
for i in r:
    if i != ' ':
        a+=1
print(a)