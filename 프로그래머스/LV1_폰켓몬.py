def solution(nums):
    length=len(nums)//2
    nums=set(nums)
    answer = min(length,len(nums))
    return answer
