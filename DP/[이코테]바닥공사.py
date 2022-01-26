#바닥공사
N=int(input())
arr=[0 for _ in range(N+1)]
arr[1]=1

if N>=2:
    arr[2]=3

for i in range(3,N+1):
    arr[i]=arr[i-1]+arr[i-2]*2

print(arr[N]%796796)
