n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
    for k in range(2*(n-i)):
        print(" ",end='')
    for p in range(i):
        print("*",end='')
    print("\n",end='')
for i in range(1,n):
    for j in range(n-i):
        print("*",end='')
    for k in range(2*i):
        print(" ",end='')
    for p in range(n-i):
        print("*",end='')
    print("\n",end='')
