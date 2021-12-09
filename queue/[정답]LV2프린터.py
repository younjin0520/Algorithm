from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    for i,priority in enumerate(priorities):
        q.append((priority,i))
    while q:
        item=q.popleft()
        
        #더 큰 수가 남아있을 때 맨 뒤로 보냄
        if q and max(q)[0]>item[0]:
            q.append(item)
        else:
            answer+=1
            if item[1]==location:
                break
    return answer
