#처음: 단순히 in을 썼을 때 시간초과
#이분탐색

import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A.sort()

M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

for num in B:
    mid=N//2
    low=0
    high=N-1
    find=False
    while low<=high:
        if A[mid]==num:
            find=True
            break
        elif A[mid]>num:
            high=mid-1
        else:
            low=mid+1
        mid=(low+high)//2
    if find==True:
        print(1)
    else:
        print(0)
