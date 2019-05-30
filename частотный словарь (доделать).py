import operator
import re
a=int(input('Число первых значений'))
full_text = open('input2.txt', 'r')
my_list = (full_text.read()).split(' ')
list_1 = []

for i in my_list:
    list_1.append(i.lower())
    
dict_1 = {}
for x in list_1:
    if x in dict_1:
        dict_1[x] += 1
    elif x not in dict_1:
        dict_1[x] = 1
sorted_dict = sorted(dict_1.items(), reverse=True, key=operator.itemgetter(1))
o=" "
for r in range(a):
    o = f'{sorted_dict[r][0]}   -  {sorted_dict[r][1]}'
    print(o)
    final = open('output.txt', 'a')
    final.write(o + '\n')
    final.close()
    

