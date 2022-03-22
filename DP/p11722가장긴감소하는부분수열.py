N=int(input())
arr=list(map(int,input().split()))
dp=[1 for _ in range(N)]

for i in range(1,N):
    maxNum=0
    for j in range(i):
        if arr[j]>arr[i] and maxNum<dp[j]:
            maxNum=dp[j]
    dp[i]=maxNum+1

print(max(dp))
