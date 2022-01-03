#boj2217_로프

import sys

N=int(sys.stdin.readline())
lope=[]
weight=[]

for i in range(N):
    lope.append(int(sys.stdin.readline()))

#역순정렬후 각각의 값에 로프수 곱하기
lope.sort(reverse=True)
for i in range(len(lope)):
    weight.append((i+1)*lope[i])

print(max(weight))
