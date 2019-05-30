import re
pal = input()
x = pal.lower()
counter=0
a_cnt=0
b_cnt=0
c_cnt=0
xcnt=0
s=[]
end=0
for i in range (0, len(x)):
    if x[i]=='a':
        a_cnt+=1
        i+=1
        s+=(x[i]+a_cnt)
        b_cnt=0
        c_cnt=0

    elif x[i]=='b':
        b_cnt+=1
        i+=1
        s+=['b', b_cnt]
        a_cnt=0
        c_cnt=0
    
    elif x[i]=='c':
        c_cnt+=1
        i+=1
        s+=['c',c_cnt]
        a_cnt=0
        
        b_cnt=0
print(s)
#print(reg.sub('', s))
#for i in [s]:
    

#pal = input()
#x = pal.lower()
#begin=0
#cnta=0
#if pal[0]=='a':
#    begin='a'
#if pal[0]=='b':
#    begin='b'
#if pal[0]=='c':
#    begin='c'
#print(begin,pal.count('a'))
#for i in pal:
#i=0
#while i<len(pal):
#    if pal[i]=='a':
#        for i in pal:
#            cnta=pal.count('a')
#i+=1
#print ('a',cnta)
#print(pal.find('a'), pal.rfind('a'))

