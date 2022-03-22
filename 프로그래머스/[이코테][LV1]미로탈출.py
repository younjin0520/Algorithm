import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,list(sys.stdin.readline().strip()))))

def dfs():
    stack=[(0,0)]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while stack:
        x,y=stack.pop()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and ny<m and nx<n and arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                stack.append((nx,ny))

dfs()
print(arr[n-1][m-1])
