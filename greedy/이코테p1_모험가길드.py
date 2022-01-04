#이것이코딩테스트다
#Greedy1_모험가길드
import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split())) #공포도를 담을 배열
arr.sort()

result=0 #최대 그룹의 수
index=-1

for i in range(len(arr)):
    #그룹에 참여하는 인원이 i번째 공포도보다 크거나 같을 때
    if (i-index)>=arr[i]:
        result+=1
        index=i

print(result)
