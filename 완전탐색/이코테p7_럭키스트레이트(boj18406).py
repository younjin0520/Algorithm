#구현
#p18406_럭키스트레이트
import sys

N=sys.stdin.readline().strip()
length=len(N)
left=0
right=0

for i in range(len(N)//2):
    left+=int(N[i])
    right+=int(N[length-1-i])

if left==right:
    print('LUCKY')
else:
    print('READY')
