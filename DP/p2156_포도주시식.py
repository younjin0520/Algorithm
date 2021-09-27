import sys
n=int(sys.stdin.readline())
arr=[]
#입력 받기
for i in range(n):
    arr.append(int(sys.stdin.readline()))

result=[0]*n
result[0]=arr[0]
if n>1:
    result[1]=arr[0]+arr[1]
if n>2:
    result[2]=max(result[1],arr[0]+arr[2],arr[1]+arr[2])

for i in range(3,n):
    #n과 n-1둘다 마실때
    t1=result[i-3]+arr[i-1]+arr[i]
    t2=result[i-1] #n-1만 마심
    t3=result[i-2]+arr[i] #n만 마심
    result[i]=max(t1,t2,t3)
print(result[n-1])
