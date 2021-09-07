import sys

s=list(sys.stdin.readline())

alpha=[26]
alpha=[0 for i in range(26)]

for i in range(len(s)-1):
    alpha[ord(s[i])-97]+=1

for i in range(26):
    print(alpha[i],end=' ')
