def solution(absolutes, signs):
    answer =0
    l=len(absolutes)
    for i in range(l):
        if signs[i]==False:
            num=absolutes[i]*-1
        else:
            num=absolutes[i]
        answer+=num
    return answer
