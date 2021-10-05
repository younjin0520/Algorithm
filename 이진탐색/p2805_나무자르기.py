import sys
n,k=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
high=max(arr)
low=1
while high>=low:
    count=0
    mid=(high+low)//2
    for i in range(n):
        count+=arr[i]//mid
    if count>=k:
        low=mid+1
    else:
        high=mid-1
print(high)
