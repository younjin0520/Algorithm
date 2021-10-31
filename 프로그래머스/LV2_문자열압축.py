def solution(s):
    #단순구현
    answer=len(s)
    #압축단위설정
    for step in range(1,(len(s)//2)+1):
        tmp=""
        short=s[:step]
        count=1
        for i in range(step,len(s),step):
            if short==s[i:i+step]:
                count+=1
            else:
                if count>1:
                    tmp+=str(count)
                tmp+=short
                count=1
            short=s[i:i+step]
        if count>1:
            tmp+=str(count)
        tmp+=short
        answer=min(answer,len(tmp))
    return answer
