import sys

n=int(sys.stdin.readline())
li=[]

for i in range(n):
    a,b=map(str,sys.stdin.readline().split())
    li.append([int(a),b])
li.sort(key=lambda x: x[0])

for i in range(n):
    print(li[i][0],li[i][1])
