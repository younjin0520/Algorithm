import sys

n,m=map(int,sys.stdin.readline().split())

def two_count(n):
    two=0
    while n!=0:
        n=n//2 #2의 배수의 개수를 구함
        two+=n
    return two

def five_count(n):
    five=0
    while n!=0:
        n=n//5
        five+=n
    return five

num1=two_count(n)-two_count(m)-two_count(n-m)
num2=five_count(n)-five_count(m)-five_count(n-m)
print(min(num1,num2))
