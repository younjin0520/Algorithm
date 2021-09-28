import sys

n=int(sys.stdin.readline())
arr=[0]*n
arr[0]=1
if n>1:
    arr[1]=3
for i in range(2,n):
    arr[i]=2*arr[i-2]+arr[i-1]
print(arr[n-1])
