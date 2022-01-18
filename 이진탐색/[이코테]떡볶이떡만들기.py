import sys
N,M=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

def cal(arr,x):
    result=0
    for item in arr:
        if item>x:
            result+=(item-x)
    return result

#이진탐색
high=max(arr)
low=0
while low<=high:
    mid=(low+high)//2
    length=cal(arr,mid)
    if length<M:
        high=mid-1
    else:
        low=mid+1

print(high)
