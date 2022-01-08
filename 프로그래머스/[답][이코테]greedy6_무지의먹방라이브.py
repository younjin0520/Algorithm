#greedy_시간이 적게 걸리는 음식부터 확인
#최소 힙 이용 - (음식 시간, 음식 번호)
#(음식 번호 * 음식 시간)만큼 빼줌
import heapq

def solution(food_times, k):
    #더이상 먹을 음식이 없을 때
    if sum(food_times)<=k:
        return -1
    
    #최소힙(우선순위 큐)에 삽입
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1)) #(음식시간,음식번호)
    
    sum_value=0 #먹기위해 사용한 시간
    previous=0 #직전에 다 먹은 음식 시간
    length=len(food_times) #남은 음식의 개수
    
    #먹은 시간+(현재 음식 시간-이전의 음식 시간)*음식 종류 수 <= k
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0] #가장 적은 시간의 음식 다 먹기
        sum_value += (now-previous)*length #이전음식을 다 먹었으므로 (현재시간 - 이전음식시간)
        length-=1 #다 먹은 음식 제외
        previous=now #이전 음식 시간 재설정
    result = sorted(q,key=lambda x:x[1]) #음식 번호 기준 정렬
    
    return result[(k-sum_value)%length][1] #남은시간 = 전체시간-먹은시간
