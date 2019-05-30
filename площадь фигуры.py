import math
z=str(input())
if (z=='прямоугольник'):
      a=float(input())
      b=float(input())
      print (a*b) 
elif (z=='треугольник'):
      a=float(input())
      b=float(input())
      c=float(input())
      p=((a+b+c)/2)
      print (math.sqrt(p*(p-a)*(p-b)*(p-c)))
elif  (z=='круг'):
      r=float(input())
      print (3.14*(r ** 2))
