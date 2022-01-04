#p4796_캠핑
import sys

count=0
while True:
    L,P,V=map(int,sys.stdin.readline().split())
    count+=1
    
    if L==0 and P==0 and V==0:
        break
    quotient=V//P
    result=quotient*L+min(V%P,L)
    print('Case '+str(count)+': '+str(result))
