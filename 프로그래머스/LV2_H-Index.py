def solution(citations):
    citations.sort(reverse=True)
    minArr=[]
    for h,citation in enumerate(citations):
        minArr.append(min(h+1,citation))
    answer=max(minArr)
    return answer
