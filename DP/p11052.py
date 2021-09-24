import sys

n=int(sys.stdin.readline())
arr=[0]+list(map(int,sys.stdin.readline().split()))
result=[0]*(n+1)

result[1]=arr[1]

for i in range(2,n+1):
    result[i]=arr[i]
    for j in range(1,i//2+1):
        result[i]=max(result[j]+result[i-j],result[i])

print(result[n])
