import sys

n=int(sys.stdin.readline())

if n==0:
    print('0')
else:
    result=''
    while n!=0:
        if n%2==0:
            result='0'+result
            n=n//-2
        else:
            result='1'+result
            n=n//-2+1
    print(result)
