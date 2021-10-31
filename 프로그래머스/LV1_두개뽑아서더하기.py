from itertools import combinations

def solution(numbers):
    numbers=list(combinations(numbers,2))
    for i,number in enumerate(numbers):
        numbers[i]=number[0]+number[1]
    
    answer = list(set(numbers))
    answer.sort()
    return answer
