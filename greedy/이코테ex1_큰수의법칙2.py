import sys
N,M,K=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

result=0
count=0
for i in range(M):
    if count<K:
        result+=arr[-1]
    else:
        result+=arr[-2]
        
    count+=1
    if count==K+1:
        count=0

print(result)
