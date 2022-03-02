#팀결성
N,M=map(int,input().split())

parent=[0 for _ in range(N+1)]
for i in range(N+1):
    parent[i]=i

def union(a,b):
    parentA=a
    parentB=b
    while parent[a]!=parentA:
        parentA=parent[a]
    while parent[b]!=parentB:
        parentB=parent[b]
    min_=min(parentA,parentB)
    parent[a]=min_
    parent[b]=min_
        
    
for _ in range(M):
    inst,a,b=map(int,input().split())
    if inst==0: #팀합치기
        union(a,b)
    else:   #같은 팀 여부 확인
        if parent[a]==parent[b]:
            print('YES')
        else:
            print("NO")
        
