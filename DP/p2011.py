import sys
arr=list(map(int,sys.stdin.readline().rstrip()))
l=len(arr)
alpha=[0]*l

if arr[0]==0:
    print('0')
    exit()

alpha[0]=1

if l>1:
    if arr[1]>0:
        alpha[1]=1
    if 10<=arr[0]*10+arr[1]<=26:
        alpha[1]+=1

for i in range(2,l):
    if arr[i]>0:
        alpha[i]+=alpha[i-1]
    if 10<=arr[i-1]*10+arr[i]<=26:
        alpha[i]+=alpha[i-2]
print(alpha[-1]%1000000)
