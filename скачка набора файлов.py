# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests
lst = []
first = str(input())
target = 'We'
second = ''
with open(first, 'r') as a:
    for line in a:
        lst.append(line.replace('\n', ''))
        second = lst[0]
        second = second[0:second.rfind("/")]
        b = requests.get(str(lst[0]))
        b = (b.text.strip(' ').splitlines())
        third = b[0]

while b[0] != target:
    b = requests.get(second +'/' + third)
    b = (b.text.strip(' ').splitlines())
    print(b)
    third = b[0]
