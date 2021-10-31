def solution(progresses, speeds):
    answer = []
    idx=0 #현재 내보내야할것
    count=0
    while True:
        if idx>=len(progresses):
            break
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
            if progresses[i]>=100 and idx==i:
                count+=1
                idx+=1
        if count>0:
            answer.append(count)
            count=0
    return answer
