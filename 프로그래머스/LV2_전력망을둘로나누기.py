#https://programmers.co.kr/learn/courses/30/lessons/86971

def checkNum(n,graph):
    result=1
    stack=[1]
    visited=[False for _ in range(n+1)]
    visited[1]=True
    
    while stack:
        num=stack.pop()
        for i in graph[num]:
            if visited[i]==False:
                stack.append(i)
                visited[i]=True
                result+=1
    return result

def solution(n, wires):
    answer = n
    graph=[[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        answer=min(answer,abs(2*checkNum(n,graph)-n))
        graph[a].append(b)
        graph[b].append(a)
    return answer
