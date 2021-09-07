n=int(input())
for i in range(n):
    if i==n-1:
        for j in range(2*n-1):
            print("*",end='')
    else:
        if i==0:
            for j in range(n-1):
                print(" ",end='')
            print("*",end='')
        else:
            for j in range(n-1-i):
                print(" ",end='')
            print("*",end='')
            for j in range(2*i-1):
                print(" ",end='')
            print("*",end='')
    print("\n",end='')
