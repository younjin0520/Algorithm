#윤년은 2월 29일까지 존재

def solution(a, b):
    date=[31,29,31,30,31,30,31,31,30,31,30,31]
    day={1:'FRI',2:'SAT',3:'SUN',4:'MON',5:'TUE',6:'WED',0:'THU'}
    for i in range(a-1):
        b+=date[i]
    answer=day[b%7]
    return answer
