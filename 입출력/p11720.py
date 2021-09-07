n=int(input())
a=int(input())
div=1
for i in range(n-1):
    div=div*10
sum=0
for i in range(n-1):
    sum=(a//div)+sum
    a=a%div
    div=div//10
print(int(sum+a))
