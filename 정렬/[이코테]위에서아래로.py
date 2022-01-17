import sys
N=int(sys.stdin.readline())
numArr=[]
for i in range(N):
    numArr.append(int(sys.stdin.readline()))
numArr.sort(reverse=True)
for n in numArr:
    print(n,end=' ')
