#dic2(신고한 사람과 신고받은 사람의 dictionary)를 만들지 않으면 출력을 위해 전체 report를 확인해야 하기때문에 시간초과 걸림

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))] #메일받은 횟수를 출력
    dic={} #각 ID가 신고받은 횟수를 저장
    dic2={} #신고한사람 저장
    report=list(set(report)) #겹치는 신고 제거
    
    for item in report:
        name1,name2=item.split()
        if name2 in dic:
            dic[name2]+=1
        else:
            dic[name2]=1
        if name1 in dic2:
            dic2[name1].append(name2)
        else:
            dic2[name1]=[name2]
            
    for i in range(len(id_list)):
        if id_list[i] not in dic2: #신고안했을때
            answer[i]=0
            continue
        for name in dic2[id_list[i]]:
            if dic[name]>=k: #k번이상 신고를 받으면 출력
                answer[i]+=1    
    return answer
