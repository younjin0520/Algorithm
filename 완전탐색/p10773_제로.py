#완전탐색
import sys
K=int(sys.stdin.readline())
arr=[]
for i in range(K):
    num=int(sys.stdin.readline())
    if num==0:
        arr=arr[:-1]
    else:
        arr.append(num)

print(sum(arr))
