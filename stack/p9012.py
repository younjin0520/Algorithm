import sys
n=int(sys.stdin.readline())

for i in range(n):
    right=0
    stack=list(sys.stdin.readline())
    for j in range(len(stack)):
        word=stack.pop()
        if (word==')'):
            right+=1
        elif (word=='('):
            right-=1
        if right<0:
            print("NO")
            break
    if right==0:
        print("YES")
    elif right>0:
        print("NO")
