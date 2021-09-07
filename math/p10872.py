import sys
count=0
n=int(sys.stdin.readline())
result=1
for i in range(1,n+1):
    result*=i

result=str(result)
while result[-1]=='0':
    count+=1
    result=result[:-1]
print(count)
