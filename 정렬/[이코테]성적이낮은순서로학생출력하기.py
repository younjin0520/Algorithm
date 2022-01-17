import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    name,score=sys.stdin.readline().strip().split()
    arr.append([name,int(score)])

arr=sorted(arr,key=lambda x:x[1])

for item in arr:
    print(item[0],end=' ')
