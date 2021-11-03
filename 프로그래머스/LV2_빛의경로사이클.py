def lotation(di,sign):
    if sign=='L':
        di=(di+1)%4
    elif sign=='R':
        di=(di-1)%4
    return di

def solution(grid):
    dx=[0,1,0,-1] #우,상,좌,하
    dy=[1,0,-1,0]
    result=[]
    dic={}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                dic[(i,j,k)]=False

    for i in range(len(grid)):
        grid[i]=list(grid[i])
        
    #시작점, 방향 설정
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for di in range(4):
                #i,j,di는 처음 점과 방향
                count=0
                d=di
                nx=i
                ny=j
                while True:
                    #다음 점으로 옮기기
                    nx=(nx+dx[d])%len(grid)
                    ny=(ny+dy[d])%len(grid[0])
                    d=lotation(d,grid[nx][ny])
                    count+=1
                    #싸이클이 돌아왔을때
                    if nx==i and ny==j and di==d:
                        result.append(count)
                        break
                    if dic[(nx,ny,d)]==True:
                        break
                    dic[(nx,ny,d)]=True
                    
    result.sort()            
    return result
