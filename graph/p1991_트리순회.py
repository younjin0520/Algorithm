import sys

n=int(sys.stdin.readline())
graph=[]
path={}
for i in range(n):
    graph.append(list(map(str,sys.stdin.readline().split())))

visited=[]
for i in range(n):
    path[graph[i][0]]=graph[i][1:]
    
#1.중위순회
def mid(x):
    visited.append(x)
    if path[x][0]!='.':
        mid(path[x][0])
    if path[x][1]!='.':
        mid(path[x][1])
    return visited

arr=mid('A')
visit=''
for i in arr:
    visit+=i
print(visit)

#2.전위순회
visited.clear()
def preorder(x,arr):
    if path[x][0]!='.':
        preorder(path[x][0],arr)
    arr.append(x)
    if path[x][1]!='.':
        preorder(path[x][1],arr)
    return arr

arr=preorder('A',visited)
visit=''
for i in arr:
    visit+=i
print(visit)

#3.후위순회
visited.clear()
def postorder(x):
    if path[x][0]!='.':
        postorder(path[x][0])
    if path[x][1]!='.':
        postorder(path[x][1])
    visited.append(x)
    return visited

arr=postorder('A')
visit=''
for i in arr:
    visit+=i
print(visit)
