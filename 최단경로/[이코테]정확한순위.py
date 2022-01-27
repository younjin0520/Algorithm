#Q38_정확한순위
#플로이드워셜 알고리즘
import sys
n,m=map(int,sys.stdin.readline().split())
arr=[[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split()) #a<b
    arr[a][b]=True
for i in range(1,n+1):
    arr[i][i]=True

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][k]==True and arr[k][j]==True:
                arr[i][j]=True

result=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if arr[i][j]==True:
            count+=1
        if arr[j][i]==True:
            count+=1
    if count==n+1:
        result+=1
print(result)
