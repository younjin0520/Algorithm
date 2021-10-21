import sys
from itertools import combinations
while True:
    arr=list(map(int,sys.stdin.readline().split()))
    if len(arr)==1:
        break
    arr=arr[1:]
    combi=list(combinations(arr,6))
    for item in combi:
        for j in item:
            print(j,end=' ')
        print()
    print()
