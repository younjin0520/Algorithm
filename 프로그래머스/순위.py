#https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    answer = 0
    strong=[set() for _ in range(n+1)]
    weak=[set() for _ in range(n+1)]
    
    for result in results:
        first,second=result[0],result[1]
        strong[second].add(first)
        weak[first].add(second)
    
    for i in range(1,n+1):
        for s in strong[i]:
            weak[s].update(weak[i])
        for w in weak[i]:
            strong[w].update(strong[i])
            
    for i in range(1,n+1):
        if len(strong[i])+len(weak[i])==n-1:
            answer+=1
    return answer
