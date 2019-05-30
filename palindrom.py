x = input()
pal = x.lower() 
a = [pal]    
aCnt = 0
bCnt = 0
cCnt = 0
i = 0
j=len(pal)-1
while i < len(a):
    pal = a[i]
    j = 0
    while j < len(pal):
        c = pal[j]
        if c == "a":
            aCnt = aCnt+1
        if c == "b":
            bCnt = bCnt+1
        if c == "c":
            cCnt = cCnt+1
        j= j+1
        i = i+1
print ('a',aCnt,'b',bCnt,'c',cCnt) 
