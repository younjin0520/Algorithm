#[구현]치킨배달
import sys
from itertools import combinations

N,M=map(int,sys.stdin.readline().split())
city=[]
for i in range(N):
    city.append(list(map(int,sys.stdin.readline().split())))

#집의 위치 저장
house=[]
chicken=[]
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append((i,j))
        elif city[i][j]==2:
            chicken.append((i,j))

combi=list(combinations(chicken,M))

#치킨거리 구하기
def cal(x1,y1,x2,y2):
    result=abs(x1-x2)+abs(y1-y2)
    return result

result=[]
#모든 조합에 대하여 치킨거리의 합 계산해보기
for cList in combi:
    tmp=0
    for x1,y1 in house:
        min_len=10000000
        for x2,y2 in cList:
            min_len=min(cal(x1,y1,x2,y2),min_len) #가장 작은 치킨거리 저장
        tmp+=min_len #모든 집의 합 구하기
    result.append(tmp)
print(min(result))
