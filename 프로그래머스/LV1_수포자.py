def solution(answers):
    a = []
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    for i,answer in enumerate(answers):
        if first[i%5]==answer:
            score[0]+=1
        if second[i%8]==answer:
            score[1]+=1
        if third[i%10]==answer:
            score[2]+=1
    max_=max(score)
    for i in range(3):
        if score[i]==max_:
            a.append(i+1)
    return a
