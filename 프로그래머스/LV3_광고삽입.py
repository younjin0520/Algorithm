def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)   
    adv_time = str_to_int(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                          
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       #시청자 수 누적하기
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 0초부터 전체 시청자 수 누적하기
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           #가장 시청자수가 많은 구간 탐색
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else: #i==adv_time-1일때
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)

#문자열을 초로 바꿔주는 함수
def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#초를 문자열로 바꿔주는 함수
def int_to_str(time):
    h = time // 3600
    time = time % 3600
    m = time // 60
    s = time % 60
    return format(h,'02') + ':' + format(m,'02') + ':' + format(s,'02')
