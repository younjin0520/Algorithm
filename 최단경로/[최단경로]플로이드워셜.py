#플로이드 워셜 알고리즘
#O(N^3)
INF=int(1e9)
#입력받기
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#각 간선 정보 그래프에 저장
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

#플로이드 워셜 알고리즘
#a에서 b로 갈때 (k는 거쳐가는 점)
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#수행된 결과를 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b],end=' ')
    print()
