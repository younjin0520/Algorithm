import sys

a,b=map(int,sys.stdin.readline().split())

def gcd(a,b):
    if a<b :
        tmp=a
        a=b
        b=tmp
    while b!=0:
        n=a%b
        a=b
        b=n
    return a

print(gcd(a,b))
print(a*b/gcd(a,b))
