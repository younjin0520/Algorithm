import sys
n=int(sys.stdin.readline())
for i in range(n):
    k=int(sys.stdin.readline())
    arr=[0]*k
    arr[0]=1
    if k>1:
        arr[1]=2
    if k>2:
        arr[2]=4
    for j in range(3,k):
        arr[j]=arr[j-1]+arr[j-2]+arr[j-3]
    print(arr[k-1])
