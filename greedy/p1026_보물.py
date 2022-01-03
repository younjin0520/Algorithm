#boj1026_보물

import sys

result=0
N=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a.sort(reverse=True)
b.sort()

for i in range(N):
    result+=a[i]*b[i]

print(result)
