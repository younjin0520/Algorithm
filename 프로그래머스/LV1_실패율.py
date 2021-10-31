def solution(N, stages):
    answer = []
    fail=[]
    #도달한 사용자 수
    game=[0]*(N+2)
    for stage in stages:
        game[stage]+=1
    
    reach=game.copy()
    for i in range(N+1,1,-1):
        reach[i-1]+=reach[i]
    for i in range(1,N+1):
        if reach[i]>0:
            fail.append((i,game[i]/reach[i]))
        else:
            fail.append((i,0))
    fail=sorted(fail,key=lambda x:(-x[1],x[0]))
    for i in range(len(fail)):
        answer.append(fail[i][0])
    return answer
