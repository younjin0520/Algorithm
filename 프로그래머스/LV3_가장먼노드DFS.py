def solution(n, edge):
    answer = 0
    path=[50001 for _ in range(n+1)]
    arr=[[] for _ in range(n+1)]
    for start,end in edge:
        arr[start].append(end)
        arr[end].append(start)
    
    path[0]=0
    path[1]=0
    
    stack=[1]
    while stack:
        x=stack.pop()
        for i in arr[x]:
            if path[i]>path[x]+1:
                stack.append(i)
                path[i]=path[x]+1
    
    max_=max(path)
    for i in range(1,n+1):
        if path[i]==max_:
            answer+=1
    return answer
