#boj1789_수들의합
#greedy_가장 작은것 부터 더할 수 있을만큼 더하기

import sys

N=int(sys.stdin.readline())
num=0

for i in range(1,N+1):
    if N-num<i:
        break
    num+=i

print(i-1)
