#1로 만들기
#값을 저장해두고 다이나믹프로그래밍 이용

N=int(input())
arr=[0 for _ in range(N+1)]
if N>=2:
    arr[2]=1
if N>=3:
    arr[3]=1
if N>=4:
    arr[4]=2
if N>=5:
    arr[5]=1
    
for i in range(6,N+1):
    result=30001
    if i%5==0:
        result=arr[i//5]+1
    if i%3==0:
        result=min(result,arr[i//3]+1)
    if i%2==0:
        result=min(result,arr[i//2]+1)
    arr[i]=min(result,arr[i-1]+1)

print(arr[N])
