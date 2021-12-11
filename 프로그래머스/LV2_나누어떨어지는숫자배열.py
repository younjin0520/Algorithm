def solution(arr, divisor):
    answer = []
    for item in arr:
        if item%divisor==0:
            answer.append(item)
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer
