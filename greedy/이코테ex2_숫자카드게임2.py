import sys
N,M=map(int,sys.stdin.readline().split())
minArr=[]
for i in range(N):
    minArr.append(min(list(map(int,sys.stdin.readline().split()))))

print(max(minArr))
