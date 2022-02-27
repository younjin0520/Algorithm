#시간초과
def solution(number, k):
    answer = ''
    idx=0
    k=len(number)-k #k는 남겨야 할 수
    while (idx<len(number) and k>0):
        now=int(number[idx])    #현재 비교할 수
        max_=idx
        #뒤에있는 조건을 만족시킬 수 있는 수 중 가장 큰 수를 찾음
        for j in range(idx+1,len(number)):
            if int(number[j])>int(number[max_]) and len(number)-j>=k:
                max_=j
        k-=1
        answer+=number[max_]
        idx=max_+1
    return answer
