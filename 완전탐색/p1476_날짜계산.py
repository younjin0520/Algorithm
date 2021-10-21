import sys
E,S,M=map(int,sys.stdin.readline().split())
count=0
while True:
    if (count%15)+1==E and (count%28)+1==S and (count%19)+1==M:
        break
    count+=1

print(count+1)
