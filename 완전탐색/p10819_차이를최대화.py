import sys
from itertools import permutations

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

combi=list(permutations(arr,n))
result=0
for item in combi:
    diff=0
    for j in range(1,n):
        diff+=abs(item[j]-item[j-1])
    result=max(result,diff)
print(result)
