def solution(s):
    answer = 0
    eng=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i,key in enumerate(eng):
        s=s.replace(key,str(i))
    answer=int(s)
    return answer
