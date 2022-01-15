def solution(a, b, g, s, w, t):
    answer = (10**9)*(10**5)*4
    length=len(w)
    low=0
    high=(10**9)*(10**5)*4
    
    while low<=high:
        mid=(high+low)//2
        gold=0
        silver=0
        total=0
        
        for i in range(length):
            time=t[i]
            gold_now=g[i]
            silver_now=s[i]
            weight=w[i]
            
            move=mid//(time*2)
            if mid%(time*2)>=time:
                move+=1
            max_weight=move*weight
            
            if gold_now<max_weight:
                gold+=gold_now
            else:
                gold+=max_weight
            if silver_now<max_weight:
                silver+=silver_now
            else:
                silver+=max_weight
            if gold_now+silver_now<max_weight:
                total+=gold_now+silver_now
            else:
                total+=max_weight
            
        if gold>=a and silver>=b and total>=a+b:
            high=mid-1
            answer=min(answer,mid)
        else:
            low=mid+1
    
    return answer