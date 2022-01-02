#greedy3_문자열뒤집기
import sys

num=sys.stdin.readline()
def zeroToOne(num):
    result=0
    if num[0]=='0':
        result+=1
    for i in range(len(num)-1):
        if num[i]=='0' and num[i+1]=='1':
            result+=1
    return result

def oneToZero(num):
    result=0
    if num[0]=='1':
        result+=1
    for i in range(len(num)-1):
        if num[i]=='1' and num[i+1]=='0':
            result+=1
    return result


print(min(zeroToOne(num),oneToZero(num)))
