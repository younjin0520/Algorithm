#개미전사
n=int(input())
arr=list(map(int,input().split()))
dp=[0 for _ in range(n)]
dp[0]=arr[0]
dp[1]=max(arr[0],arr[1])

for i in range(2,n):
    dp[i]=max(dp[i-2]+arr[i],dp[i-1])
print(dp[n-1])
