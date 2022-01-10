#누적합

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    arr=[]
    arr.append((1,0))
    arr.append((0,1))
    for i in range(2,N+1):
        zero=arr[i-1][0]+arr[i-2][0]
        one=arr[i-1][1]+arr[i-2][1]
        arr.append((zero,one))
    print(arr[N][0],arr[N][1])
