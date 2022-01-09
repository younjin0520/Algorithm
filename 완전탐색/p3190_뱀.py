#p3190_뱀
from collections import deque
import sys
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
board=[[0 for _ in range(N)] for _ in range(N)]
direction=[(-1,0),(0,1),(1,0),(0,-1)] #상우하좌(시계방향)
turn={}
result=0
nowX,nowY,nowD=0,0,1
q=deque() #뱀이 현재 있는 경로를 저장할 큐

#사과표시:1
for _ in range(K):
    x,y=map(int,sys.stdin.readline().split())
    board[x-1][y-1]=1

#방향저장
L=int(sys.stdin.readline())
for _ in range(L):
    time,d=map(str,sys.stdin.readline().strip().split())
    time=int(time)
    if d=='D': #오른쪽회전
        d=1
    else: #왼쪽회전
        d=-1
    turn[time]=d

board[0][0]=-1
q.append((0,0))
#이동하기
while True:
    if result in turn:
        nowD=(nowD+turn[result])%4
    result+=1
    #규칙1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
    nowX+=direction[nowD][0]
    nowY+=direction[nowD][1]
    #끝나는 조건: 벽에 닿거나 자기자신의 몸에 닿거나
    if nowX<0 or nowX>=N or nowY<0 or nowY>=N or board[nowX][nowY]==-1:
        break
    q.append((nowX,nowY))
    #규칙2. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
    if board[nowX][nowY]!=1:
       a,b=q.popleft()
       board[a][b]=0
    board[nowX][nowY]=-1
print(result)
