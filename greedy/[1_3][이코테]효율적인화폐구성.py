import sys
n,m=map(int,sys.stdin.readline().split())
coins=[]
result=[0 for _ in range(m+1)]

for _ in range(n):
    coins.append(int(sys.stdin.readline()))
for coin in coins:
    if coin<=m:
        result[coin]=1

for i in range(1,m+1):
    if result[i]>0:
        for coin in coins:
            if i+coin<=m and (result[i+coin]==0 or result[i+coin]>result[i]+1):
                result[i+coin]=result[i]+1

if result[m]==0:
    print(-1)
else:
    print(result[m])
