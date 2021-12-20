def solution(n):
    #약수는 1과 자기자신을 포함
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i
    return answer
