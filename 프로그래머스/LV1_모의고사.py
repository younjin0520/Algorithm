def solution(answers):
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    
    count=[0]*3
    
    for i,answer in enumerate(answers):
        if first[i%5]==answer:
            count[0]+=1
        if second[i%8]==answer:
            count[1]+=1
        if third[i%10]==answer:
            count[2]+=1
    
    max_=max(count)
    result=[]
    for i in range(len(count)):
        if count[i]==max_:
            result.append(i+1)
    return result
