from itertools import combinations
def solution(nums):
    answer = 0
    arr=list(combinations(nums,3))
    for i,tup in enumerate(arr):
        arr[i]=tup[0]+tup[1]+tup[2]
    
    #소수판별
    for num in arr:
        flag=True
        for i in range(2,int(num**(1/2)+1)):
            if num%i==0:
                flag=False
                break
        if flag:
            answer+=1
    return answer
