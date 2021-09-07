import sys

s=list(sys.stdin.readline())

alpha=[26]
alpha=[-1 for i in range(26)]

for i in range(len(s)-1):
    num=alpha[ord(s[i])-97]
    if(num==-1):
        alpha[ord(s[i])-97]=i

for i in alpha:
    print(i,end=' ')
