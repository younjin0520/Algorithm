#Greedy2_곱하기 혹은 더하기

import sys
numArr=list(map(int,sys.stdin.readline().strip()))  #붙어있는 숫자 배열로 바꾸기

result=0

for idx in range(len(numArr)):
    result+=numArr[idx]
    if result>0:
        break

for i in range(idx+1,len(numArr)):
    if numArr[i]!=0 or numArr[i]!=1:
        result*=numArr[i]
    else:
        result+=numArr[i]
print(result)
