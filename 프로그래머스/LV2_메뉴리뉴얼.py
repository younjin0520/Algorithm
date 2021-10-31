from itertools import combinations #조합
from collections import Counter #각 원소의 중복 횟수를 세어줌

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c) #모든 조합의 경우의 수를 tuple의 형태로 반환
            temp += combi
        #모든 주문에 대해 시행하고 겹치는 원소를 반환
        counter = Counter(temp)
        if counter: #조건을 만족시키는 counter가 존재할 때
            m=max(counter.values())
            if m>=2:
                for key,value in counter.items():
                    if value==m:
                        answer.append(''.join(key))
    return sorted(answer)
