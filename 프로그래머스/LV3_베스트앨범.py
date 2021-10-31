def solution(genres, plays):
    l=len(genres)
    dic={}
    s={}
    answer=[]
    for i in range(l):
        if genres[i] in dic:
            dic[genres[i]].append((i,plays[i]))
            s[genres[i]]+=plays[i]
        else:
            dic[genres[i]]=[(i,plays[i])]
            s[genres[i]]=plays[i]
    s=dict(sorted(s.items(), key=lambda x:-x[1]))
    print(s)
    for key in dic.keys():
        dic[key]=sorted(dic[key], key=lambda x:-x[1])
    for key in s.keys():
        answer.append(dic[key][0][0])
        if len(dic[key])>1:
            answer.append(dic[key][1][0])
    return answer
