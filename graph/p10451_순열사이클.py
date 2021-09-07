import sys

t=int(sys.stdin.readline())

def dfs(arr,start,visit):
    num=arr[start]
    visit[start]=True
    while num!=start+1:
        visit[num-1]=True
        num=arr[num-1]
        
for i in range(t):
    count=0
    n=int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    visit=[False for i in range(n)]
    for j in range(n):
        if visit[j]==False:
            count+=1
            dfs(arr,j,visit)
    print(count)
    
        
