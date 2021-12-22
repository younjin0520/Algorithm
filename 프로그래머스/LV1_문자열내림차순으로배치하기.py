def solution(s):
    answer = ''
    arr=[]
    for alpha in s:
        arr.append(ord(alpha))
        
    arr.sort(reverse=True) #역순정렬하기
    
    for i in range(len(arr)):
        answer+=chr(arr[i])
    return answer
