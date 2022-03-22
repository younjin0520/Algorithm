#https://programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    if len(a)==1:
        return 1
    elif len(a)==2:
        return 2
    
    answer = 2
    length = len(a)
    leftToRight = [False for _ in range(length)]
    rightToLeft = [False for _ in range(length)]
    
    minLeft = a[0]
    minRight = a[length-1]
    
    for i in range(1,length-1):
        if minLeft>a[i]:
            leftToRight[i] = True
            minLeft = a[i]
        
        if minRight>a[length-1-i]:
            rightToLeft[length-1-i] = True
            minRight = a[length-1-i]

    for i in range(1, length-1):
        if leftToRight[i]==False and rightToLeft[i]==False:
            continue
        else:
            answer+=1
    return answer
