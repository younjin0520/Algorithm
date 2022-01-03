#boj10162_전자레인지
#greedy

import sys
N=int(sys.stdin.readline())
a=0
b=0
c=0
#시간을 정확히 맞출 수 없는 경우
if N%10>0:
    print(-1)
    exit()

while N>0:
    if N>=300:
        N-=300
        a+=1
    elif N>=60:
        N-=60
        b+=1
    else:
        N-=10
        c+=1

print(a,b,c)
