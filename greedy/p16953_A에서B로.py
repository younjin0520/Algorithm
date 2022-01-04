import sys

result=1
a,b=map(int,sys.stdin.readline().split())

while b>=a:
    if b==a:
        print(result)
        exit()
    if b%2==0:
        b//=2
        result+=1
    else:
        if b%10==1:
            b//=10
            result+=1
        else:
            break
print('-1')
