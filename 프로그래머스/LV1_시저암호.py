def solution(s, n):
    answer = ''
    for alpha in s:
        #알파벳이 아닐때: 그대로 더하기
        if alpha.isalpha()==False:
            answer+=alpha
            continue
            
        #대문자일때
        if ord(alpha)<=90:
            new=ord(alpha)+n #알파벳 to 아스키코드
            if new>90:
                new-=26
                
        #소문자일때
        else:
            new=ord(alpha)+n
            if new>122:
                new-=26
                
        answer+=chr(new) #아스키코드 to 알파벳
            
    return answer
