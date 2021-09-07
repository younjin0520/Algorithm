import sys
sys.setrecursionlimit(10**9)
n=int(sys.stdin.readline())
head=[0 for i in range(n+1)]
graph=[[] for i in range(n+1)]
head[1]=1
for i in range(n-1):
    start,end=map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(start,tree,parents):
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            dfs(i,tree,parents)

dfs(1,graph,head)

for i in range(2,n+1):
    print(head[i])
