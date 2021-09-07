import sys

#1.그래프로만들기
n,m=map(int,sys.stdin.readline().split())
graph=[[] for i in range(n+1)]
visit=[False for i in range(n+1)]
count=0
for i in range(m):
    start,end=map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n+1):
    graph[i].sort()

#2.탐색하기 DFS
def dfs(start):
    stack=[]
    stack.append(start)

    while stack:
        node=stack.pop()
        if visit[node]==False:
            visit[node]=True
            stack.extend(reversed(graph[node]))

#3. 연결리스트 세기
for i in range(1,n+1):
    if visit[i]==False:
        count+=1
        dfs(i)
print(count)

    
