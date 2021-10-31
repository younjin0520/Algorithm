def enter(id_,dic):
    s=dic[id_]+'님이 들어왔습니다.'
    return s
def leave(id_,dic):
    s=dic[id_]+'님이 나갔습니다.'
    return s

def solution(record):
    answer = []
    dic={}
    #닉네임 고치기
    for i in range(len(record)):
        if record[i].split()[0]=='Leave':
            continue
        li=list(record[i].split())
        inst,id_,nick=li[0],li[1],li[2]
        if inst=='Enter' or inst=='Change':
            dic[id_]=nick
    
    #출력하기
    for r in record:
        inst,id_,nick=r[0],r[1],r[2]
        if r.split()[0]=='Enter':
            answer.append(enter(r.split()[1],dic))
        elif r.split()[0]=='Leave':
            answer.append(leave(r.split()[1],dic))
    return answer
