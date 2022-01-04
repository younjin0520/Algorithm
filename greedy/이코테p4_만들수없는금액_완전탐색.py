#greedy4_만들수없는금액
#완전탐색으로 풀이

import sys
from itertools import combinations

N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
combi=[]
count=1

#금액의 모든 조합만들기
for i in range(1,len(arr)+1):
    tmp=list(combinations(arr,i))
    for j in range(len(tmp)):
        combi.append(sum(tmp[j]))

combi.sort()
combi=set(combi) #겹치는 금액 제거

#없는금액 찾기
for item in combi:
    if item!=count:
        break
    count+=1
print(count)
