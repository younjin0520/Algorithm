import sys

stack=list(sys.stdin.readline())
num=0
pre=0
s=0
for i in stack:
    if i=='(':
       pre=1
       num+=1
    elif i==')':
        num-=1
        if pre==1:
            pre=0
            s+=num
        else:
            s+=1

print(s)
        
