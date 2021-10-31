def solution(lottos, win_nums):
    answer = []
    min_=0
    max_=0
    zero=0
    lottos.sort()
    for lotto in lottos:
        if lotto==0:
            zero+=1
    for i in range(len(win_nums)):
        for j in range(zero,len(lottos)):
            if lottos[j]==win_nums[i]:
                min_+=1
                break
    if min_==0:
        min_=1
    min_=7-min_
    max_=min_-zero
    if max_==0:
        max_=1
    answer.append(max_)
    answer.append(min_)
    return answer
