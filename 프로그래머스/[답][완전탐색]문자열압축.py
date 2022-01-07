#압축안한것이 가장짧을때도 고려해줄것
#나머지 처리

def solution(s):
    answer = len(s)
    
    #압축할 문자열의 수
    for i in range(1,len(s)//2+1):
        count=1
        result=""
        word=s[0:i] #첫 단어
        for j in range(i,len(s),i):
            if word==s[j:j+i]:
                count+=1
            else:
                if count>1:
                    result+=str(count)+word
                else:
                    result+=word
                word=s[j:j+i]
                count=1
        #나머지 처리
        if count>1:
            result+=str(count)+word
        else:
            result+=word
        answer=min(answer,len(result))
    return answer
