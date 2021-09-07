import sys
from collections import deque

queue=deque()
n=int(sys.stdin.readline())

for i in range(n):
    s=sys.stdin.readline()
    if(' ' in s):
        a,b=s.split()
    else:
        a=s
    
    if 'push_back' in a:
        queue.append(int(b))
    elif 'push_front' in a:
        queue.appendleft(int(b))      
    elif 'pop_front' in a:
        if len(queue)!=0:
            print(queue.popleft())
        else:
            print("-1")
    elif 'pop_back' in a:
        if len(queue)!=0:
            print(queue.pop())
        else:
            print("-1")
    elif 'size' in a:
        print(len(queue))
    elif 'empty' in a:
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif 'front' in a:
        if len(queue)==0:
            print("-1")
        else:
            print(queue[0])
    elif 'back' in a:
        if len(queue)==0:
            print("-1")
        else:
            print(queue[-1])
