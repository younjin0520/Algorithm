#플로이드 워셜 알고리즘 이용
import sys
INF=int(1e9)
n,m=map(int,sys.stdin.readline().split())
arr=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    arr[i][i]=0
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a][b]=1
    arr[b][a]=1
x,k=map(int,sys.stdin.readline().split())

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j]>arr[i][k]+arr[k][j]:
                arr[i][j]=arr[i][k]+arr[k][j]

if arr[1][k]==INF or arr[k][x]==INF:
    print(-1)
else:
    print(arr[1][k]+arr[k][x])
