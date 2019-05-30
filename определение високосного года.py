a = int(input())
if 1900<=a<=3000:
  if (a % 4 == 0) and (a % 100 != 0) or (a % 400 ==0):
    print('Високосный')
  else:
    print('Обычный')
else:
  print('недопустимое значение')
