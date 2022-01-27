#개선된 다익스트라 알고리즘
#O(ElogV) E는 간선의 개수 V는 노드의 개수
#최단 거리가 가장 짧은 노드를 빠르게 찾음 (힙)
import heapq
import sys
input =sys.stdin.readline
INF=int(1e9)

#입력받기
n,m=map(int,input().split()) #노드의 개수, 간선의 개수
start=int(input()) #시작노드번호 입력
graph=[[] for i in range(n+1)] #각 노드의 연결 정보
distance=[INF]*(n+1) #최단 거리 테이블
#모든 간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) #a에서 b로가는 비용 c

def dijkstra(start):
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now]<dist: #이미 처리된 노드일 때 무시
            continue
        #현재 노드와 인접한 노드 확인
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

#최단거리 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
