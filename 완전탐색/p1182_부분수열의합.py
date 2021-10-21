import sys
from itertools import combinations

N,S=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
count=0
for i in range(1,N+1):
    combi=list(combinations(arr,i))
    for j in combi:
        s=0
        for k in j:
            s+=k
        if s==S:
            count+=1
print(count)
