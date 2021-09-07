import sys

a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
d=1
num=0
result=[]
for i in range(m-1,-1,-1):
    num+=arr[i]*d
    d*=a

while num!=0:
    result.append(num%b)
    num//=b

for i in range(1,len(result)+1):
    print(result[len(result)-i],end=' ')
