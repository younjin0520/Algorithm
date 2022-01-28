#화성탐사_DFS이용

import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    graph=[]
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))

    #DFS이용
    stack=[(0,0)]
    new_graph=[[100001]*N for _ in range(N)]
    new_graph[0][0]=graph[0][0]
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    while stack:
        x,y=stack.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and new_graph[nx][ny]>new_graph[x][y]+graph[nx][ny]:
                stack.append((nx,ny))
                new_graph[nx][ny]=new_graph[x][y]+graph[nx][ny]
    print(new_graph[N-1][N-1])
