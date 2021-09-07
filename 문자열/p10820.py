import sys

lines=sys.stdin.readlines()
num=0
blank=0
s=0
b=0

for line in lines:
    num=0
    blank=0
    s=0
    b=0
    line=list(line)
    for i in line:
        if i.isdigit():
            num+=1
        elif i.isalpha():
            if ord(i)<97:
                b+=1
            else:
                s+=1
        elif i==' ':
            blank+=1
    print(s,b,num,blank)
