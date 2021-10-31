def change1(num):
    result=''
    while num>0:
        result+=str(num%3)
        num=num//3
    return result

def change2(num):
    result=0
    length=len(num)
    for i in range(length):
        result+=int(num[length-1-i])*(3**i)
    return result
def solution(n):
    tmp=change1(n)
    answer=change2(tmp)
    return answer
