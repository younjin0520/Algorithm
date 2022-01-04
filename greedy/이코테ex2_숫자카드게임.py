import sys
n,m=map(int,sys.stdin.readline().split())
cards=[]
for i in range(n):
    cards.append(min(list(map(int,sys.stdin.readline().split()))))
print(max(cards))
