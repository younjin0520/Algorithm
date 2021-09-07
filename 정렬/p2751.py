import sys

n=int(input())
a=[]
for i in range(n):
    word=int(sys.stdin.readline())
    a.append(word)
a.sort()
for i in a:
    print(i)
