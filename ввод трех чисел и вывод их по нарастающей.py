a=int(input())
b=int(input())
c=int(input())
if a > b and a > c and b < a and b < c:
     print (a)
     print (b)
     print (c)
elif a == c and c > b and a > b:
     print (a)
     print (b)
     print (c)
elif a == b and b > c and a > c:
     print (a)
     print (c)
     print (b)
elif b == c and b > a and c > a:
     print (b)
     print (a)
     print (c)
elif c == b and b == a and c == a:
     print (c)
     print (b)
     print (a)
elif a == c and c < b and a < b:
     print (b)
     print (a)
     print (c)
elif a == b and b < c and a < c:
     print (c)
     print (a)
     print (b)
elif b == c and b < a and c < a:
     print (a)
     print (b)
     print (c)     
elif a > b > c:
     print (a)
     print (c)
     print (b)
elif c > a > b:
     print (c)
     print (b)
     print (a)
elif c > b > a:
     print (c)
     print (a)
     print (b)
elif b > c > a:
     print (b)    
     print (a)
     print (c)
elif b > a > c:
     print (b)    
     print (c)
     print (a)
