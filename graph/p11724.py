import sys
n,m=map(int,sys.stdin.readline().split())

li=[0 for i in range(1001)]
count=1
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    if li[a]!=0 and li[b]==0:
        li[b]=li[a]
    elif li[b]!=0 and li[a]==0:
        li[a]=li[b]
    elif li[b]!=0 and li[a]!=0:
        if li[a]>li[b]:
            big=li[a]
            count-=1
            for j in range(1001):
                if li[j]==big:
                    li[j]=li[b]
        elif li[a]<li[b]:
            big=li[b]
            count-=1
            for j in range(1001):
                if li[j]==big:
                    li[j]=li[a]
    else:
        li[a]=li[b]=count
        count+=1

for i in range(1,n+1):
    if li[i]==0:
        count+=1
print(count-1)
