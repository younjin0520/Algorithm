#https://www.acmicpc.net/problem/1065

N = int(input())
answer = 0
arr = [str(i+1) for i in range(N)]

for i in range(N):
    num = arr[i]
    isTrue = True
    
    if len(num)==1:
        answer+=1
        continue
    elif len(num) == 2:
        answer+=1
        continue

    past = int(num[1])
    diff = int(num[1])-int(num[0])
    
    for j in range(2,len(num)):
        if int(num[j])-past!=diff:
            isTrue = False
            break
        past = int(num[j])

    if isTrue == True:
        answer+=1

print(answer)
