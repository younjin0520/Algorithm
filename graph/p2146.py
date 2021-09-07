import sys
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1

#섬구분
def bfs(x,y):
    q=deque()
    q.append((x,y))
    arr[x][y]=count
    visit[x][y]=True
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if arr[nx][ny]==1 and visit[nx][ny]==False:
                visit[nx][ny]=True
                arr[nx][ny]=count
                q.append((nx,ny))

def bfs2(count):
    q=deque()
    dist=[[-1]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j]==count:
                q.append((i,j))
                dist[i][j]=0 #거리저장
                
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            #다른 땅을 만났을 때
            if arr[nx][ny]>0 and arr[nx][ny]!=count:
                return min(answer,dist[x][y])
            #바다를 만났을 때
            if arr[nx][ny]==0 and dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
                
#입력 받기
n=int(sys.stdin.readline())
arr=[]
visit=[[False]*n for i in range(n)]
answer=10000
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visit[i][j]==False:
            bfs(i,j)
            count+=1

for i in range(1,count):
    answer=bfs2(i)

print(answer)
