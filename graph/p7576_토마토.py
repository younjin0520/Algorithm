import sys
from collections import deque

m,n=map(int,sys.stdin.readline().split())
tomato=[]
result=0
one=deque()

#1.입력받기
for i in range(n):
    tomato.append(list(map(int,sys.stdin.readline().split())))
    for j in range(m): #익은 토마토를 큐에 넣어줌
        if tomato[i][j]==1:
            one.append((i,j))
#2.bfs
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(queue):
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[x][y]+1
                queue.append((nx,ny))

bfs(one)
for i in tomato:
    for j in i:
        if j==0:
            print('-1')
            exit()
    result=max(result,max(i))
print(result-1)
