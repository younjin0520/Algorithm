import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
up=[1]*n
down=[1]*n
s=[0]*n

for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            up[i]=max(up[i],up[j]+1)

    
    for j in range(i):
        if arr[n-1-i]>arr[n-1-j]:
            down[n-1-i]=max(down[n-1-i],down[n-1-j]+1)
for i in range(n):
    s[i]=up[i]+down[i]-1
print(max(s))
