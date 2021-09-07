import sys

n=int(sys.stdin.readline())
new=[]
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    new.append([a,b])
new.sort(key=lambda x: (x[1],x[0]))
for i in range(n):
    print(new[i][0],new[i][1])
