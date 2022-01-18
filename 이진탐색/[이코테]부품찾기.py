#이진탐색_p2부품찾기
import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))

arr.sort()
#이진탐색
for item in arr2:
    isHere=False
    low=0
    high=N-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==item:
            isHere=True
            break
        elif arr[mid]>item:
            high=mid-1
        else:
            low=mid+1
    if isHere==True:
        print('yes',end=' ')
    else:
        print('no',end=' ')
