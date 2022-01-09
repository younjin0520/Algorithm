#이코테 예제4-2
#시각_완전탐색 풀이

n=int(input())
hour=0
minute=0
second=0
result=0

#시간이 될 때까지 초를 하나씩 증가시키며 반복
while hour<=n:
    #3이 포함되어 있는지 확인
    if hour//10==3 or hour%10==3 or minute//10==3 or minute%10==3 or second//10==3 or second%10==3:
        result+=1
    second+=1
    #60초가 넘었을 때
    if second==60:
        minute+=1
        second=0
    #60분을 넘었을 때
    if minute==60:
        minute=0
        hour+=1
print(result)
