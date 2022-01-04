import sys
n,m,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

num=arr[-1]*k+arr[-2]

print(num*(m//k)+arr[-1]*m%k)
