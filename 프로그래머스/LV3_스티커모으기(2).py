import copy
def solution(sticker):
    answer = 0
    if len(sticker)==1:
        return sticker[0]
    elif len(sticker)==2:
        return max(sticker)
    
    useFirst = [False for _ in range(len(sticker))]
    dp1=copy.deepcopy(sticker) #첫 번째 원소 사용
    dp2=copy.deepcopy(sticker) #마지막 원소 사용
    
    dp1[2]+=dp1[0]
    
    for i in range(3,len(sticker)-1):
        dp1[i]+=max(dp1[i-3:i-1])
    for i in range(len(sticker)-3,0,-1):
        dp2[i]+=max(dp2[i+2:i+4])
        
    max1=max(dp1)
    max2=max(dp2)
    answer=max(max1,max2)
    return answer
