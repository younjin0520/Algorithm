def solution(id_list, report, k):
    dic={}  #신고받은 사람과 신고인을 저장
    mail={}
    for item in report:
        name1, name2 = item.split()
        if name2 not in dic:
            dic[name2]=[name1]
        elif name1 not in dic[name2]:
            dic[name2].append(name1)
    
    for id in id_list:
        mail[id]=0
        
    for names in dic.values():
        if len(names)>=k:
            for name in names:
                mail[name]+=1
                
    answer=list(mail.values())
    return answer
