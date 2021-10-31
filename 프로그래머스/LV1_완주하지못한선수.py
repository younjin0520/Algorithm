def solution(participant, completion):
    answer=''
    participant.sort()
    completion.sort()
    l=len(completion)
    for i in range(l):
        if participant[i]!=completion[i]:
            answer=participant[i]
            break
    if answer=='':
        answer=participant[-1]
    return answer
