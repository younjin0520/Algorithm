def solution(dirs):
    answer = 0
    dic = {"U":[-1,0], "L":[0,-1], "D":[1,0],"R":[0,1]}
    visited = []
    x,y=0,0
    
    for d in dirs:
        nx = dic[d][0]+x
        ny = dic[d][1]+y
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        if (x,y,nx,ny) not in visited:
            visited.append((x,y,nx,ny))
            visited.append((nx,ny,x,y))
            answer+=1
        x = nx
        y = ny
    return answer
