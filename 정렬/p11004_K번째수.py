import sys
n,k=map(int,sys.stdin.readline().split())
li=list(map(int,input().split()))
li.sort()
print(li[k-1])
