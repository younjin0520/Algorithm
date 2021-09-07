import sys
from math import gcd
t=int(sys.stdin.readline())

for i in range(t):
    arr=list(map(int,sys.stdin.readline().split()))
    arr=arr[1:]
    sum=0
    for j in range(len(arr)):
        for k in range(j+1,len(arr)):
            sum+=gcd(arr[j],arr[k])
    print(sum)
