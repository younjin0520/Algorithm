def solution(d, budget):
    d.sort()
    d.insert(0,0)
    d.append(0)
    
    for i in range(1,len(d)):
        d[i]+=d[i-1]
        
    for i in range(len(d)):
        if budget<d[i]:
            break
    return i-1
