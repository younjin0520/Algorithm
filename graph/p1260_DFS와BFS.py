import sys
from collections import deque

n,m,v=map(int,sys.stdin.readline().split())
graph=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a][b]=graph[b][a]=1
    
def dfs(start):
    visit=[]
    stack=[]
    stack.append(start)
    while stack:
        node=stack.pop()
        if node not in visit:
            visit.append(node)
            print(node,end=' ')
            for i in range(n,0,-1):
                if graph[node][i]==1:
                    stack.append(i)

def bfs(start):
    visit=[]
    queue=deque()
    queue.append(start)
    while queue:
        node=queue.popleft()
        if node not in visit:
            visit.append(node)
            print(node,end=' ')
            for i in range(1,n+1):
                if graph[node][i]==1:
                    queue.append(i)

dfs(v)
print()
bfs(v)
