spisok = [10, 9, 7, 66, 77, 55, 11, 0, -2, -10, -11, 0.6]

a = spisok[0]
for i in spisok:
    if i < a:
        a = i
print ('наименьшее число этого списка:', a)