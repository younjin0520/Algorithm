import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
dp=[0]*n
dp[0]=1
for i in range(1,n):
    tmp=[0]
    for j in range(i):
        if arr[i]>arr[j]:
            tmp.append(dp[j])
    dp[i]=max(tmp)+1
print(max(dp))
