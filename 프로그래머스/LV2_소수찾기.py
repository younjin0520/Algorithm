from itertools import permutations

def solution(numbers):
    numArr=list(numbers)
    arr=[]
    arr2=set()
    for i in range(1,len(numArr)+1):
        arr.extend(permutations(numArr,i))
    answer=0
    for item in arr:
        num=''
        for j in item:
            num+=j
        arr2.add(int(num))
    #소수찾기
    for item in arr2:
        flag=True
        for j in range(2,int(item**(1/2)+1)):
            if item%j==0:
                flag=False
                break
        if flag==True and item>1:
            answer+=1
                
    return answer
