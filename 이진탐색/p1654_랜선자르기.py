import sys

k,n=map(int,sys.stdin.readline().split())
arr=[]
for i in range(k):
    arr.append(int(sys.stdin.readline()))
m=max(arr)
s=1

while m>=s:
    mid=(m+s)//2
    count=0
    for i in arr:
        count+=i//mid

    if count<n:
        m=mid-1
    else:
        s=mid+1
print(m)
