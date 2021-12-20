def solution(n):
    answer = 0
    n=str(n) #int to string
    for i in n:
        answer+=int(i)
    return answer
