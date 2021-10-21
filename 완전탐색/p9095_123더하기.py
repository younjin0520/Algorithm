import sys

T=int(sys.stdin.readline())
for i in range(T):
    n=int(sys.stdin.readline())
    arr=[0]*n
    arr[0]=1
    if n>1:
        arr[1]=2
    if n>2:
        arr[2]=4
    for j in range(3,n):
        arr[j]=arr[j-1]+arr[j-2]+arr[j-3]
    print(arr[n-1])
