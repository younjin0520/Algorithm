import sys
x,y=map(int,sys.stdin.readline().split())

def cal(n):
    return ((y+n)*100)//(x+n)

low=0
high=x
winper=cal(0)
answer=-1

while low<=high:
    mid=(low+high)//2
    result=cal(mid)
    if winper<result:
        high=mid-1
        answer=mid        
    else:
        low=mid+1

print(answer)        
