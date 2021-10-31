def solution(new_id):
    answer = ''
    #1.소문자 치환
    answer=new_id.lower()
    #2.특수문자 제거
    for i in answer:
        if i.isalnum() or i=='-' or i=='_' or i=='.':
            continue
        answer=answer.replace(i,"")
    #3.연속된 마침표 제거
    while '..' in answer:
        answer=answer.replace('..',".")
    #4.처음이나 끝 마침표 제거
    if answer[0]=='.':
        answer=answer[1:]
    if len(answer)>0 and answer[-1]=='.':
        answer=answer[:-1]
    #5. 빈 문자열이면 a대입
    if answer=='':
        answer='a'
    #6. 16자 이상이면 15개만 남기기
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    #7. 2자 이하라면 길이가 3이 될 때까지 마지막 문자 반복
    while len(answer)<=2:
        answer=answer+answer[-1]
    return answer
