#p1946_신입사원
#서류점수, 면접점수가 모두 다른 사람보다 낮으면 안됨
#시간초과 이유: 모든 이전 사람들의 면접순위와 비교하는 것이 아니라 최솟값과 비교하기

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    N=int(sys.stdin.readline())
    score=[]
    result=N

    #입력받기
    for i in range(N):
        a,b=map(int,sys.stdin.readline().split())
        score.append((a,b))
    score.sort() #0열을 기준으로 정렬
    
    minNum=score[0][1]
    #비교하기
    for i in range(N):
        if minNum<score[i][1]:
            result-=1
        else:
            minNum=score[i][1]
    print(result)
