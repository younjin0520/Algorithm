import sys
has=[]
a,p=map(int,sys.stdin.readline().split())
if p==1:
    print('0')
    exit()
    
count=0
num=0

def cal(a,p):
    sum=0
    a=list(map(int,str(a)))
    for i in range(len(a)):
        sum+=a[i]**p
    return sum

has.append(a)
num=cal(a,p)
while num not in has:
    has.append(num)
    num=cal(num,p)
    count+=1
for i in range(len(has)):
    if has[i]==num:
        break
print(i)
