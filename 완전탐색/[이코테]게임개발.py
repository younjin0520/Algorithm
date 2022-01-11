#게임개발
#책(이코테)의 예제
import sys

N,M=map(int,sys.stdin.readline().split())
x,y,d=map(int,sys.stdin.readline().split()) #현재 위치와 방향
arr=[]
direction=[[-1,0],[0,1],[1,0],[0,-1]] #북동남서
result=0

#바다:1 육지:0 가본곳:-1
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr[x][y]=-1
while True:
    for i in range(4):
        #1.현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 갈 곳을 정한다
        nx=x+direction[(d-1)%4][0] #세로
        ny=y+direction[(d-1)%4][1] #가로
        #2. 가보지 않은 칸이 존재할 경우 -> 왼쪽으로 회전 후 한칸 이동
        if (nx>=0 and nx<N and ny>=0 and ny<M) and arr[nx][ny]==0:
            x=nx
            y=ny
            arr[x][y]=-1
            break
        d=(d-1)%4
    #네 방향 모두 가본 칸이거나 바다일 경우 -> 바라보는 방향을 유지한 채로 한 칸 뒤로 이동 후 1단계로 돌아감    
    if i==3:
        #한칸뒤로가기
        nx=x+direction[(d+2)%4][0]
        ny=y+direction[(d+2)%4][1]
        if nx>=0 and ny>=0 and nx<N and ny<M and arr[nx][ny]!=1:
            x=nx
            y=ny
            arr[x][y]=-1
        else:
            break

#방문한 칸의 수 출력
for num in arr:
    for n in num:
        if n==-1:
            result+=1
print(result)
