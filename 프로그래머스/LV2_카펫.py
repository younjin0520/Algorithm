def solution(brown, yellow):
    answer = []
    #yellow의 약수 구하기 (가능한 세로길이)
    high=[1]
    for i in range(2,yellow//2+1):
        if yellow%i==0:
            high.append(i)
    for h in high:
        r=yellow//h
        num=(2*r)+(2*h)+4
        if num==brown:
            return [r+2,h+2]
