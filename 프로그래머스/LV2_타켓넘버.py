def dfs(numbers,target):
    stack=[(numbers[0],0),(-numbers[0],0)]
    count=0
    while stack:
        node,depth=stack.pop()
        if depth==len(numbers)-1:
            if node==target:
                count+=1
            continue
        stack.append((node+numbers[depth+1],depth+1))
        stack.append((node-numbers[depth+1],depth+1))
    return count

def solution(numbers, target):
    return dfs(numbers,target)
