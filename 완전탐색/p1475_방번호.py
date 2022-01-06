#p1475_방번호
#key: 각 숫자의 개수를 셀 때 9를 6으로 취급해주기

import sys
import math
arr=[0 for _ in range(10)]
s=sys.stdin.readline().strip()

for num in s:
    if num=='9':
        arr[6]+=1
    else:
        arr[int(num)]+=1

arr[6]=max(1,math.ceil(arr[6]/2))#올림함수

print(max(arr))
