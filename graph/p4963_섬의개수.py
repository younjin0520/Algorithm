import sys
from collections import deque
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
#1.bfs
def bfs(graph,a,b):
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    while queue:
        x,y=queue.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=h or nx<0 or ny>=w or ny<0:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0
                
w,h=map(int,sys.stdin.readline().split())

while w!=0 or h!=0:
    count=0
    graph=[]
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for i in range(w):
        for j in range(h):
            if graph[j][i]==1:
                bfs(graph,j,i)
                count+=1
    print(count)
    
    w,h=map(int,sys.stdin.readline().split())
