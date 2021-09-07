import sys

n,b=map(int,sys.stdin.readline().split())
result=''
while n>0:
    div=n%b
    if div>=10:
        div=chr(div+55)
    result+=str(div)
    n=n//b
print("".join(reversed(result)))
