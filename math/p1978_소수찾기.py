import sys

n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
count=n

for i in range(n):
    num=arr[i]
    if num==1:
        count-=1
        continue
    for j in range(2,int(num**(1/2)+1)):
        if num%j==0:
            count-=1
            break
print(count)
