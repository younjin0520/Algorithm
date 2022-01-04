#boj1541_잃어버린 괄호
#틀린 이유: 괄호를 한 번만 칠 수 있는줄 알았는데 여러번 치는 것이 가능

import sys

result=0
string=sys.stdin.readline().strip()

numArr=list(string.split('-'))
result+=sum(list(map(int,numArr[0].split('+')))) #첫번째 숫자 더하기
for i in range(1,len(numArr)):
    result-=sum(list(map(int,numArr[i].split('+')))) #나머지 숫자 빼기

print(result)
