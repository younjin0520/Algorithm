#미로탈출
import sys
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,sys.stdin.readline().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))

def bfs():
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
bfs()
print(graph[n-1][m-1])
