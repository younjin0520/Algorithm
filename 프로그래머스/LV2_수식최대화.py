from itertools import permutations
def solution(expression):
    answer = 0
    op=['*','+','-']
    arr=[]
    s=''
    #한번에 하는법 찾아보기
    for e in expression:
        if e not in op:
            s+=e
        else:
            arr.append(int(s))
            arr.append(e)
            s=''
    arr.append(int(s))
    order=list(permutations(op))
    
    for i in range(len(order)):
        tmp=arr.copy()
        for k in range(3):
            oper=order[i][k]
            j=1
            while True:
                if j==len(tmp)-1:
                    break
                if tmp[j]==oper:
                    if oper=='*':
                        tmp[j-1]*=tmp[j+1]
                        tmp.pop(j)
                        tmp.pop(j)
                        tmp.append(0)
                        tmp.append(0)
                    elif oper=='+':
                        tmp[j-1]+=tmp[j+1]
                        tmp.pop(j)
                        tmp.pop(j)
                        tmp.append(0)
                        tmp.append(0)
                    elif oper=='-':
                        tmp[j-1]-=tmp[j+1]
                        tmp.pop(j)
                        tmp.pop(j)
                        tmp.append(0)
                        tmp.append(0)
                else:
                    j+=1
        answer=max(answer,abs(tmp[0]))
    return answer
