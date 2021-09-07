import sys

t=int(sys.stdin.readline())

def dfs(start):
    global count
    stack=[start]
    while stack:
        node=stack.pop()
        if visit[node]==False:
            cycle.append(node)
            visit[node]=True
            num=arr[node]-1
            if num in cycle: #사이클 존재
                count+=len(cycle[cycle.index(num):])
            stack.append(num)
for i in range(t):
    count=0
    n=int(sys.stdin.readline())
    arr=list(map(int, sys.stdin.readline().split()))
    visit=[False for i in range(n)]
    for j in range(n):
        if visit[j]==False:
            cycle=[]
            dfs(j)
    print(n-count)
