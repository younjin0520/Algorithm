#최단거리를 찾기위해 bfs이용
#dfs 이용 시 시간 초과 - 이 유형의 최단경로 찾기는 BFS이용하
#https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def bfs(maps):
    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) or maps[nx][ny]!=1:
                continue
            q.append((nx,ny))
            maps[nx][ny]=maps[x][y]+1
            
    if maps[-1][-1]<=1:
        return -1
    else:
        return maps[-1][-1]
    
def solution(maps):
    answer = bfs(maps)
    return answer
