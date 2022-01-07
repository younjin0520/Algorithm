#리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n=len(a) #행길이 계산
    m=len(a[0]) #열길이 계산
    result=[[0]*n for _ in range(m)] #결과 리스트 (행렬길이 뒤집음)
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result

#자물쇠 중간 부분이 모두 1인지 확인
#new_lock은 자물쇠에 열쇠를 더한 값
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    #가운데에 자물쇠 집어넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]
            
    #4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                #자물에 열쇠를 끼워넣기
                for i in range(m):
                    for j in range(n):
                        new_lock[x+i][y+j]+=key[i][j]
                
                #자물쇠가 맞는지 검사
                if check(new_lock)==True:
                    return True
                #자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
        return False
        
    answer = True
    return answer
