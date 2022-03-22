#https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = deque()
    timeLog = deque()
    idx = 0
    time = 0
    complete = 0
    while True:
        if complete == len(truck_weights):
            break
            
        if timeLog and timeLog[0]+bridge_length==time:
            onBridge.popleft()
            timeLog.popleft()
            complete+=1
            
        if idx<len(truck_weights) and len(onBridge)<bridge_length and sum(onBridge)+truck_weights[idx]<=weight:
            onBridge.append(truck_weights[idx])
            timeLog.append(time)
            idx+=1
        
        time+=1
        
    return time
