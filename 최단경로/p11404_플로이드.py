import sys

INF=int(1e9)
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
bus=[[INF]*(n+1) for _ in range(n+1)] #버스정보저장

for i in range(1,n+1):
    bus[i][i]=0
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if bus[a][b]>c:
        bus[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if bus[i][j]>bus[i][k]+bus[k][j]:
                bus[i][j]=bus[i][k]+bus[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j]==INF:
            print(0,end=' ')
        else:
            print(bus[i][j],end=' ')
    print()
