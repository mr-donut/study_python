#Открываем текстовой файл. сразу же уменьшаем регистр, заменяем табуляцию на "", разделяем по словам.
text = open('test.txt').read().replace('\n', '').lower().strip().split()
list_1 = []
#Добавляем в словарь все содержимое текста
dict = {}
key = ''
val = int
dict_1 = {}

for key in text:
    key = key.lower()
    if key in dict_1:
        val = dict_1[key]
        dict_1[key]=val+1
    else:
        dict_1[key]=1

list_1 = list(dict_1.items())

list_1.sort(key=lambda i:i[1], reverse=True)

print(list_1)