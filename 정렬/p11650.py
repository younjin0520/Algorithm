import sys

n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    li.append([a,b])
li.sort()
for i in range(n):
    print(li[i][0],li[i][1])
