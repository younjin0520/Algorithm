import sys

n=int(sys.stdin.readline())
arr=[1]*10

for i in range(n-1):
    for j in range(1,10):
        arr[j]=arr[j-1]+arr[j]
s=0
for i in range(10):
    s+=arr[i]
print(s%10007)
