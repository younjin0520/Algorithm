#다익스트라 - 간단한 버전
#노드의 개수가 5000개 이하일 때
import sys

input=sys.stdin.readline
INF=int(1e9)
n,m=map(int,input().split()) #노드의 개수, 간선의 개수
start=int(input()) #시작 노드 번호
graph=[[] for i in range(n+1)] #각 노드의 연결 정보를 담는 리스트
visited=[False]*(n+1) #방문체크
distance=[INF]*(n+1) #최단 거리 테이블

#모든 간선 정보 입력
for _ in range(m):
    a,b,c=map(int,input().split()) #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]
    #n-1번 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now=get_smallest_node()
        visited[now]=True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost=distance[now]+j[1]
            #현재 노드를 거치는게 더 짧은 경우 업데이트
            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

#최단 거리 출력
for i in range(1,n+1):
    #도달할 수 없는 경우 무한대
    if distance[i]==INF:
        print('INFINITY')
    else:
        print(distance[i])
