#https://programmers.co.kr/learn/courses/30/lessons/12978

INF=int(1e9)
def solution(N, road, K):
    answer = 0
    arr=[[INF for _ in range(N)] for _ in range(N)]
    dijkstra=[INF for _ in range(N)]
    visited=[False for _ in range(N)]
    
    dijkstra[0]=0
    visited[0]=True
    now = 0
    for a,b,c in road:
        if arr[a-1][b-1]>c:
            arr[a-1][b-1]=c
            arr[b-1][a-1]=c

    
    for i in range(N):
        idx=-1
        min_=INF
        for j in range(N):
            if visited[j]==False and dijkstra[j]>arr[now][j]+dijkstra[now]:
                dijkstra[j]=arr[now][j]+dijkstra[now]
        for j in range(N):
            if visited[j]==False and min_>dijkstra[j]:
                min_=dijkstra[j]
                idx=j
        now=idx
        visited[idx]=True
    
    for i in range(N):
        if dijkstra[i]<=K:
            answer+=1
    return answer
