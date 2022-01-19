import sys

n,x=map(int,sys.stdin.readline().split())
numArr=list(map(int,sys.stdin.readline().split()))

#n이상의 값이 나오기 시작할 때 인덱스 구하기
def binarySearch(x):
    low=0
    high=n-1
    result=0
    while low<=high:
        mid=(low+high)//2
        if numArr[mid]<x:
            low=mid+1
        else:
            result=mid
            high=mid-1
    return result

start=binarySearch(x)
count=0
for i in range(start,n):
    if numArr[i]==x:
        count+=1
    else:
        break

if count==0:
    print(-1)
else:
    print(count)
