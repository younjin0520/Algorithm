def solution(number, k):
    answer = ''
    arr=[]
    for i in range(len(number)):
        for j in range(i+1,min(i+1+k,len(number))):
            if number[i]<number[j]:
                arr.append(i)
                k-=1
                break
                
    arr.sort(reverse=True)
    number=list(number)    
    for i in arr:
        number.pop(i)
    answer=''.join(number)
    return answer
