def solution(rows, columns, queries):
    arr=[[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    answer=[]
    #회전하기
    for x1,y1,x2,y2 in queries:
        tmp=arr[x1-1][y1-1]
        mini=tmp
        #왼쪽
        for k in range(x1-1,x2-1):
            arr[k][y1-1]=arr[k+1][y1-1]
            mini=min(mini,arr[k+1][y1-1])
        #아래
        for k in range(y1-1,y2-1):
            arr[x2-1][k]=arr[x2-1][k+1]
            mini=min(mini,arr[x2-1][k+1])
        #오른쪽
        for k in range(x2-1,x1-1,-1):
            arr[k][y2-1] = arr[k-1][y2-1]
            mini = min(mini, arr[k-1][y2-1])
        #위
        for k in range(y2-1,y1-1,-1):
            arr[x1-1][k] = arr[x1-1][k-1]
            mini = min(mini, arr[x1-1][k-1])
        arr[x1-1][y1]=tmp
        #최솟값 찾기
        answer.append(mini)
    return answer
