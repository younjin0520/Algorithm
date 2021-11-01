import sys
n,m=map(int,sys.stdin.readline().split())
graph=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))

def dfs(i,j):
    stack=[(i,j)] #루트집어넣기
    while stack:#스택확인
        x,y=stack.pop()#꺼내기
        if graph[x][y]==1: #방문제크
            continue
        graph[x][y]=1 #방문하기
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            stack.append((nx,ny))

count=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            count+=1
            dfs(i,j)

print(count)
