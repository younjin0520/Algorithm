#누적합문제_단순계산시 시간초과

import sys
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.insert(0,0)
#누적합
for i in range(1,n+1):
    arr[i]+=arr[i-1]
    
for _ in range(m):
    result=0
    start,end=map(int,sys.stdin.readline().split())
    print(arr[end]-arr[start-1])
