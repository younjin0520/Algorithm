def solution(board, moves):
    answer = 0
    n=len(board)
    new=[[] for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(n):
            if board[i][j]>0:
                new[j].append(board[i][j])
    stack=[]
    for move in moves:
        if new[move-1]:
            stack.append(new[move-1].pop())

    flag=True
    while flag and stack:
        flag=False
        pre=stack[0]
        for k in range(1,len(stack)):
            if pre==stack[k]:
                stack.pop(k)
                stack.pop(k-1)
                answer+=2
                flag=True
                break
            pre=stack[k]
    return answer
