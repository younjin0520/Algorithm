def solution(s):
    answer = True
    if len(s)==4 or len(s)==6:
        for item in s:
            if item.isdigit()==False:
                answer=False
    else:
        answer=False
    return answer
