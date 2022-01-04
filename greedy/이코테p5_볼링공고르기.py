#greedy5_볼링공고르기

import sys

result=0
N,M=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

for i in range(len(arr)-1):
    now=arr[i]
    for j in range(i+1,len(arr)):
        if now==arr[j]:
            continue
        result+=1
        
print(result)
