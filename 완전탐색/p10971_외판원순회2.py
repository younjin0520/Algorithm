import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
print(arr)
