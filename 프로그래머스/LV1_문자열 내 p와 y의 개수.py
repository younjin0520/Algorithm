def solution(s):
    answer = True
    pCount=0
    yCount=0
    
    for alpha in s:
        if alpha=='p' or alpha=='P':
            pCount+=1
        elif alpha=='y' or alpha=='Y':
            yCount+=1
    if pCount!=yCount:
        answer=False
    return answer
