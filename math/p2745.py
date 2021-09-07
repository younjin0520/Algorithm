import sys

n,b=map(str,sys.stdin.readline().split())
sum=0
for i in range(len(n)-1,-1,-1):
    if n[i].isalpha:
        n[i]=ord(n[i])-55
    sum+=int(n[i])*int(b)    
print(sum)
