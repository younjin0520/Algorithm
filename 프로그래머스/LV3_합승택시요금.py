def solution(n, s, a, b, fares):
    inf=int(1e9)
    #1.그래프를 나타내는 배열 초기화
    path=[[inf for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        path[i][i]=0
    for fare in fares:
        path[fare[0]][fare[1]]=fare[2]
        path[fare[1]][fare[0]]=fare[2]
    
    
    #2.플루이드 알고리즘
    for i in range(1,n+1): #거쳐갈 노드
        for j in range(1,n+1): #출발 노드
            for k in range(j+1,n+1): #도착 노드
                temp=min(path[j][k],path[j][i]+path[i][k])
                path[j][k]=path[k][j]=temp
    answer=inf
    for t in range(1,n+1):
        m=path[s][t]+path[t][a]+path[t][b]
        answer=min(answer,m)
    return answer
