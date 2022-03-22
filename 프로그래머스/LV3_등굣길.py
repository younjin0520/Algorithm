def solution(m, n, puddles):
    answer=0
    arr = [[1 for _ in range(m)] for _ in range(n)]

    for y,x in puddles:
        arr[x-1][y-1] = 0

    for i in range(1,n):
        if arr[i][0]!=0:
            arr[i][0] = arr[i-1][0]
    for j in range(1,m):
        if arr[0][j]!=0:
            arr[0][j] = arr[0][j-1]
    
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][j]==0:
                continue
            arr[i][j] = arr[i][j-1] + arr[i-1][j]
            
    answer=arr[n-1][m-1]%1000000007
    
    return answer
