import sys
N=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

card.sort()
result=[0]*M

for i in range(M):
    num=arr[i]
    low=0
    high=N-1
    while high>=low:
        mid=(high+low)//2
        if card[mid]==num:
            result[i]=1
            break
        elif card[mid]>num:
            high=mid-1
        else:
            low=mid+1
for i in result:
    print(i,end=' ')
            
        
