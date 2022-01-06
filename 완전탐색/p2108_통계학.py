import sys
from collections import Counter

n=int(sys.stdin.readline())
arr=[]
result1=0
result2=0
result3=0
result4=0

for i in range(n):
    arr.append(int(sys.stdin.readline()))

result1=int(round(sum(arr)/len(arr),0)) #1.소수 첫째자리에서 반올림한 평균값
result4=max(arr)-min(arr)
arr.sort()
result2=arr[len(arr)//2] #중앙값

counter=dict(Counter(arr))
counter=sorted(counter.items(),key=lambda x:(-x[1],x[0]))
if len(counter)>1 and counter[0][1]==counter[1][1]:
    result3=counter[1][0]
else:
    result3=counter[0][0]

print(result1)
print(result2)
print(result3)
print(result4)
