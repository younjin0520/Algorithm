import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
ice=0
for _ in range(n):
    arr.append(list(map(int,list(sys.stdin.readline().strip()))))

#0은 구멍 1은 칸막이
def dfs(x,y):
    stack=[(x,y)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while stack:
        a,b=stack.pop()
        arr[a][b]=1
        for i in range(4):
            nx=dx[i]+a
            ny=dy[i]+b
            if nx>=0 and ny>=0 and nx<n and ny<m and arr[nx][ny]==0:
                stack.append((nx,ny))

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            dfs(i,j)
            ice+=1
print(ice)
