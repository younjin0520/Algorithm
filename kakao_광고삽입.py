play_time="02:03:55"
adv_time="00:14:15"
logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
def solution(play_time, adv_time, logs):
    answer = ''
    ad_start=0
    ad_end=int(adv_time[0:2])*3600+int(adv_time[3:5])*60+int(adv_time[6:8])
    ad_time=ad_end
    time=int(play_time[0:2])*3600+int(play_time[3:5])*60+int(play_time[6:8])
    
    new_log=[[] for _ in range(len(logs))]
    tag=[]
    #로그 숫자로 저장
    for i in range(len(logs)):
        s,e=map(str,logs[i].split('-'))
        new_log[i].append(int(s[0:2])*3600+int(s[3:5])*60+int(s[6:8]))
        new_log[i].append(int(e[0:2])*3600+int(e[3:5])*60+int(e[6:8]))
        diff=new_log[i][1]-ad_time
        tag.append(new_log[i][0])
        if diff>0:
            tag.append(diff)    
    max_time=0
    new_log.sort()
    tag.sort()
    idx=0  
    while ad_end<=time:
        count=0
        log_time=0
        for i in range(len(new_log)):
            log_start=new_log[i][0]
            log_end=new_log[i][1]
            
            #현재 구간안에 시청하고 있을 때
            if ad_end>log_start and ad_start<log_end:
                log_time+=min(log_end-log_start,log_end-ad_start,ad_end-log_start,ad_end-ad_start)
                
        if max_time<log_time:
            max_time=log_time
            answer=ad_start
            
        jump=time
        #시간계산
        for i in range(idx,len(tag)):
            if tag[i]>ad_start:
                idx=i
                jump=tag[i]
                break
        ad_start=jump
        ad_end=jump+ad_time
        idx+=1
    #공익광고 시작시간 반환
    hour=answer//3600
    miniute=(answer%3600)//60
    sec=answer%60
    answer=format(hour,'02')+":"+format(miniute,'02')+":"+format(sec,'02')
    return answer

print(solution(play_time,adv_time,logs))
