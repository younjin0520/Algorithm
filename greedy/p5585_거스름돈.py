#boj5585_거스름돈
#greedy_큰 잔돈부터 주기

import sys

price=int(sys.stdin.readline())
balance=1000-price
result=0

while balance>0:
    if balance>=500:
        balance-=500
    elif balance>=100:
        balance-=100
    elif balance>=50:
        balance-=50
    elif balance>=10:
        balance-=10
    elif balance>=5:
        balance-=5
    else:
        balance-=1
    result+=1

print(result)
