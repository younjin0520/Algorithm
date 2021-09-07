import sys

s=sys.stdin.readline()

li=[]
for i in range(len(s)-1):
    li.append(s[i:])
li.sort()
for word in li:
    print(word,end='')
