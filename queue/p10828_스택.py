import sys

n=int(sys.stdin.readline())

stack=[]

for i in range(n):
    s=sys.stdin.readline()

    if 'push' in s:
         s,num=map(str,s.split())
         stack.append(int(num))
    elif 'pop' in s:
        if len(stack)==0:
            print('-1')
        else:
            print(stack.pop())
    elif 'size' in s:
        print(len(stack))
    elif 'empty' in s:
        if len(stack)==0:
            print('1')
        else:
            print('0')
    elif 'top' in s:
        if len(stack)==0:
            print('-1')
        else:
            print(stack[-1])
