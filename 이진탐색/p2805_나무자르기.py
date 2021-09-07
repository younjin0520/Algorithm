import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

large=max(arr)
small=1
result=0

while small<=large:
    mid=(large+small)//2
    tree=sum([i-mid if mid<i else 0 for i in arr])
    if tree>=m:
        result=mid
        small=mid+1
    elif tree<m:
        large=mid-1
print(result)
