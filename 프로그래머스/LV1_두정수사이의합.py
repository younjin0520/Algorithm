def solution(a, b):
    answer = 0
    
    #b가 더 크게 바꾸기
    if a>b:
        a,b=b,a
        
    for i in range(a,b+1):
        answer+=i
    return answer
