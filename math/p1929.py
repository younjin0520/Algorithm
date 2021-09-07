import sys

m,n=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n+1):
    arr.append(i)
print(arr)
for i in range(2,n):
    for j in range(i+i,n+1,i):
        if arr[j]==0:
            continue
        if arr[j]%i==0:
            arr[j]=0

for i in range(m,n+1):
    if arr[i]!=0:
        print(arr[i])
