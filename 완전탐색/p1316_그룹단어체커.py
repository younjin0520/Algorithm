#풀이 방법: 이전 글자와 비교하여 다른 글자가 나오면 배열에 넣어두고 이미 배열에 존재하면 False

import sys
N=int(sys.stdin.readline())
count=0
for _ in range(N):
    word=sys.stdin.readline().strip()
    result=True
    arr=[]
    pre=word[0]
    arr.append(pre)
    for w in word:
        if pre==w:
            continue
        else:
            if w in arr:
                result=False
                break
            else:
                pre=w
                arr.append(pre)
    if result==True:
        count+=1
print(count)
