import sys

n,b=map(str,sys.stdin.readline().split())

n=list(n)
b=int(b)
result=0
p=1
for i in range(len(n)-1,-1,-1):
    if n[i].isalpha():
        n[i]=ord(n[i])-55
    else:
        n[i]=int(n[i])
    result+=n[i]*p
    p*=b
print(result)
