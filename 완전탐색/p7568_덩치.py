#완전탐색_2중 for문사용

import sys

N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    arr.append([x,y,1])
    
for i in range(N):
    for j in range(N):
        if arr[i][1]<arr[j][1] and arr[i][0]<arr[j][0]:
            arr[i][2]+=1

for i in range(N):
    print(arr[i][2],end=' ')
