import sys

n=int(sys.stdin.readline())
count=[0]*(n+1)
count[1]=0
for i in range(2,n+1):
    if i%3==0 and i%2==0:
        count[i]=min(count[i-1],count[i//3],count[i//2])+1
    elif i%3!=0 and i%2==0:
        count[i]=min(count[i-1],count[i//2])+1
    elif i%2!=0 and i%3==0:
        count[i]=min(count[i-1],count[i//3])+1
    else:
        count[i]=count[i-1]+1

print(count[n])
