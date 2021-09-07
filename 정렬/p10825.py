import sys

n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a,b,c,d=map(str,sys.stdin.readline().split())
    li.append([a,int(b),int(c),int(d)])
li.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in range(n):
    print(li[i][0])
