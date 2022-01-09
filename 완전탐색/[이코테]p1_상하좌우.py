import sys
N=int(sys.stdin.readline())
direction=list(map(str,sys.stdin.readline().split()))
x=1
y=1

for d in direction:
    if d=='R' and x+1<=N:
        x+=1
    elif d=='L' and x-1>=1:
        x-=1
    elif d=='U' and y-1>=1:
        y-=1
    elif d=='D' and y+1<=N:
        y+=1

print(y,x)
        
