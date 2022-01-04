#Greedy
#최대한많이나누기

import sys
N,K=map(int,sys.stdin.readline().split())
count=0
while N>1:
    if N>=K and N%K==0:
        N=N//K
    else:
        N-=1
    count+=1
print(count)
