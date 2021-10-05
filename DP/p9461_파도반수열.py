import sys

t=int(sys.stdin.readline())
for j in range(t):
    n=int(sys.stdin.readline())
    dp=[0]*n
    dp[0]=1
    if n>1:
        dp[1]=1
    if n>2:
        dp[2]=1

    for i in range(3,n):
        dp[i]=dp[i-2]+dp[i-3]
    print(dp[n-1])
