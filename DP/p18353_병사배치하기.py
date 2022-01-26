#가장 긴 감소하는 부분 수열

n=int(input())
arr=list(map(int,input().split()))
arr.reverse() #배열을 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 전환

dp=[1]*n
#가장 긴 증가하는 부분 수열 알고리즘
for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))
