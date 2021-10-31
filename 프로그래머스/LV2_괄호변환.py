def check(u): #올바른 문자열인지 확인
    count=0
    for i in range(len(u)):
        if u[i]=='(':
            count+=1
        else:
            count-=1
        if count<0:
            return False
    return True

def fun(p):
    result=''
    #1.빈문자열이면 빈문자열 반환
    if p=='':
        return p
    #2.w를 두 균형잡힌 문자열 u,v로 분리 //u는 균형잡힌 문자열로 더이상 분리불가
    u=''
    v=''
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            u+=p[i]
            count+=1
        elif p[i]==')':
            u+=p[i]
            count-=1
        if i>0 and count==0 and i<len(p)-1:
            v=p[i+1:]
            break
    #3.
    if check(u):
        result+=u
        result+=fun(v)
        return result
    else:
        tmp='('
        tmp+=fun(v)
        tmp+=')'
        u=u[1:-1]
        for i in u:
            if i=='(':
                tmp+=')'
            else:
                tmp+='('
        return tmp

def solution(p):
    answer=fun(p)
    return answer
