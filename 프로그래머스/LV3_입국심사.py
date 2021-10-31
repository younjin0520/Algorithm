def solution(n, times):
    answer = 0
    low=min(times)
    high=max(times)*n
    while low<high:
        mid=(low+high)//2
        people=0
        for time in times:
            people+=mid//time
        if people>=n:
            high=mid
        else:
            low=mid+1
    answer=high
    return answer
