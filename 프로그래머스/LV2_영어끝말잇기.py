#https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    person=0
    turn=0
    
    arr=[] #이미 나온 단어 넣기
    for i,word in enumerate(words):
        if word in arr or (i>0 and words[i-1][-1]!=word[0]):
            turn=i
            break
        arr.append(word)

    if turn!=0:
        person=(turn%n)+1
        turn=(turn//n)+1
    answer=[person,turn]
    return answer
