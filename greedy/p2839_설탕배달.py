#boj2839_설탕배달

import sys

N=int(sys.stdin.readline())
result=0


while N>0:
    #5로 나눠지거나 아무것도 안나눠질때 - 5로 나누기
    #3으로만 나누어질때 - 3으로 나누기
    if N%5!=0 and N%3==0:
        N-=3
        result+=1
        continue
    N-=5
    result+=1

if N==0:
    print(result)
else:
    print(-1)
