N=int(input())
numArr=list(map(int,input().split()))
result=-1

left=0
right=N-1

while left<=right:
    mid=(left+right)//2
    if mid==numArr[mid]:
        result=mid
        break
    elif mid>numArr[mid]:
        left=mid+1
    else:
        right=mid-1
        

print(result)
