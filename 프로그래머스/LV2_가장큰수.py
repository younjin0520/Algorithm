def solution(numbers):
    numbers=list(map(str,numbers))
    numbers=sorted(numbers,key=lambda x:x*3,reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))
