n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

#누적합
for x in range(1,n):
    arr[x][0]+=arr[x-1][0]
    for y in range(1,x):
        arr[x][y]+=max(arr[x-1][y-1],arr[x-1][y])
    arr[x][x]+=arr[x-1][x-1]

#최댓값 찾기
result=0
for i in range(n):
    result=max(arr[n-1][i],result)
print(result)
