from itertools import combinations
def make_dic(info):
    dic={}
    for i in info:
        li=[]
        tmp=list(i.split())
        score=int(tmp[-1])
        tmp=tmp[:-1]
        for j in range(5):
            li+=list(combinations(tmp,j))
        for k in li:
            if k in dic:
                dic[k].append(score)
            else:
                dic[k]=[score]
    return dic
def solution(info, query):
    answer = []
    dic=make_dic(info)
    for key in dic:
        dic[key].sort()
    for q in query:
        q=q.replace('and ',"")
        q=q.replace('- ',"")
        tmp=tuple(q.split())
        score=int(tmp[-1])
        tmp=tmp[:-1]
        if tmp in dic:
            new=dic[tmp]
        else:
            answer.append(0)
            continue
        
        #이분탐색
        low=0
        high=len(new)-1
        while low<=high:
            mid=(low+high)//2
            if score>new[mid]:
                low=mid+1
            else:
                high=mid-1
        answer.append(len(new)-low)
    return answer
