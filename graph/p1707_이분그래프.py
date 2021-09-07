import sys
from collections import deque

k=int(sys.stdin.readline())

def bfs(start):
    queue=deque()
    queue.append(start)
    color[start]=0
    while queue:
        node=queue.popleft()
        for i in graph[node]:
             if color[i]==-1:
                color[i]=(color[node]+1)%2
                queue.append(i)
             else:
                 if color[i]==color[node]:
                    return False              
    return True
        
for i in range(k):
    t=True
    v,e=map(int,sys.stdin.readline().split())
    graph=[[]for i in range(v+1)]
    color=[-1 for i in range(v+1)]
    for j in range(e):
        start,end=map(int,sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    for j in range(1,v+1):
        if color[j]==-1 and bfs(j)==False:
            t=False
    graph.clear()
    if t==True:
        print('YES')

    elif t==False:
        print('NO')
