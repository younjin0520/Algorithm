import sys
N,K=map(int,sys.stdin.readline().split())
arrA=list(map(int,sys.stdin.readline().split()))
arrB=list(map(int,sys.stdin.readline().split()))
arrA.sort()
arrB.sort(reverse=True)

for i in range(K):
    if arrA[i]>arrB[i]:
        break
    arrA[i],arrB[i]=arrB[i],arrA[i]
print(sum(arrA))
