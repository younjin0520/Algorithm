from collections import deque

def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n)]
    visit=[False for _ in range(n)]
    
    for start,end in edge:
        graph[start-1].append(end-1)
        graph[end-1].append(start-1)

    q=deque()
    q.append((0,0))
    arr=[]
    while q:
        node,count=q.popleft()
        if visit[node]==False:
            visit[node]=True
            arr.append((node,count))
            #print(node,count)
            for next in graph[node]:
                q.append((next,count+1))
    max_=0
    for i,j in arr:
        if max_<j:
            max_=j
            
    for i,j in arr:
        if max_==j:
            answer+=1
    return answer
