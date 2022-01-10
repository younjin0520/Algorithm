#만나는 점의 개수를 직접 계산하지 않고 반지름과 중심사이의 거리로 계산
#모든 경우의 수 생각하기

import sys

T=int(sys.stdin.readline())

for _ in range(T):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    #같은 점일때
    if x1==x2 and y1==y2:
        if r1!=r2:
            print(0)
        else:
            print(-1)
    #다른점일때
    else:
        #중심사이의 거리계산
        length=((x1-x2)**2+(y1-y2)**2)**(1/2)
        if length==r2+r1 or length==abs(r2-r1):
            print(1)
        elif length>r2+r1 or length<abs(r2-r1):
            print(0)
        else:
            print(2)

        
