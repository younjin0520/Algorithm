import sys
n=int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
result=[0]*(n+1)
result[1]=arr[0]

for i in range(2,n+1):
    tmp=[arr[i-1]]
    for j in range(1,i//2+1):
        tmp.append(result[j]+result[i-j])
    result[i]=max(tmp)
print(result[n])
