import sys
r,c=map(int,sys.stdin.readline().split())
arr=[]
words=[]
visit=[[False]*c for _ in range(r)]

for i in range(r):
    arr.append(list(sys.stdin.readline().strip()))

#가로낱말
def dfs(x,y):
    stack=[(x,y)]
    result=''
    while stack:
        a,b=stack.pop()
        visit[a][b]=True
        result+=arr[a][b]
        if b+1>=c or arr[a][b+1]=='#':
            break
        stack.append((a,b+1))
    return result
    
#세로낱말
def dfs2(x,y):
    stack=[(x,y)]
    result=''
    while stack:
        a,b=stack.pop()
        visit[a][b]=True
        result+=arr[a][b]
        if a+1>=r or arr[a+1][b]=='#':
            break
        stack.append((a+1,b))
    return result

for i in range(r):
    for j in range(c):
        if visit[i][j]==False and arr[i][j]!='#':
            word=dfs(i,j)
            if len(word)>1:
                words.append(word)
visit=[[False]*c for _ in range(r)]       
for i in range(r):
    for j in range(c):
        if visit[i][j]==False and arr[i][j]!='#':
             word=dfs2(i,j)
             if len(word)>1:
                words.append(word)
words.sort()
print(words[0])
