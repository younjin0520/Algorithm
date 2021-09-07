import sys
from collections import deque

n=int(sys.stdin.readline())
c=0
#1.bfs 함수 구현
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(graph,a,b):
    queue=deque()
    queue.append((a,b))
    graph[a][b]=0
    count=1 #집의 개수
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0
                count+=1
    return count

arr=[[] for i in range(n)]
li=[]
for i in range(n):
    arr[i]=list(map(int,sys.stdin.readline().rstrip()))
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            c+=1
            li.append(bfs(arr,i,j))
li.sort()
print(c)
for i in li:
    print(i)
