def solution(strings, n):
    answer = []
    #알파벳 순으로 정렬된 배열을 n번째 수로 다시 정렬
    answer=sorted(sorted(strings),key=lambda x:x[n])
    return answer
