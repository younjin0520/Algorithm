#DP_못생긴수
#이코테Q35
n=int(input())
numArr=[2,3,5]
arr=[False]*100000000
arr[0]=True
arr[1]=True

for num in numArr:
    for i in range(1,len(arr)):
        if arr[i]==True and i*num<len(arr):
            arr[i*num]=True

count=0
idx=0
while count<=n:
    if arr[idx]==True:
        count+=1
    idx+=1

print(idx-1)
