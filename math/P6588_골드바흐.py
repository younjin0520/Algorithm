import sys

n=1
flag=0

def is_prime_number(n):#에라토스테네스의 체
    arr = [True for i in range(n+1)]
    for i in range(2, int(n**(1/2))+1):
        if arr[i]==True:
            j=2
            while i*j<=n:
                arr[i*j]=False
                j+=1
    return arr

arr=is_prime_number(1000000)
while n!=0:
    n=int(sys.stdin.readline())
    flag=0
    for i in range(2, n//2+1):
        if arr[i]==True &arr[n-i]==True:
            print(n,'=',i,'+',n-i)
            flag=1
            break
    if flag==0 and n!=0:
        print("Goldbach's conjecture is wrong.")
