#금광_다이나믹 프로그래밍
T=int(input())

for _ in range(T):
    n,m=map(int,input().split())
    
    #행렬 나눠담기
    tmp=list(map(int,input().split()))
    arr=[]
    for i in range(0,n*m,m):
        arr.append(tmp[i:i+m])

    for y in range(1,m):
        arr[0][y]+=max(arr[0][y-1],arr[1][y-1])
        for x in range(1,n-1):
            arr[x][y]+=max(arr[x-1][y-1],arr[x][y-1],arr[x+1][y-1])
        arr[n-1][y]+=max(arr[n-2][y-1],arr[n-1][y-1])

    result=0
    #최대값 뽑아내기 - 특정 열의 최대값을 뽑아내는 방법 다시찾아보기
    for row in arr:
            max_=max(row)
            result=max(max_,result)
    print(result)

    #특정 열의 최댓값을 뽑아내는 방법 - 책의 경우
    #for i in range(n):
    #   result=max(result,dp[i][m-1])
    
