def distance(hand,num):
    pad={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2],10:[3,0],11:[3,1],12:[3,2]}
    count=abs(pad[hand][0]-pad[num][0])+abs(pad[hand][1]-pad[num][1])
    return count

def solution(numbers, hand):
    answer = ''
    nowL=10
    nowR=12
    isHand=True
    if hand=="right":
        isHand=False
        
    for num in numbers:
        if num==1 or num==4 or num==7:
            answer+='L'
            nowL=num
        elif num==3 or num==6 or num==9:
            answer+='R'
            nowR=num
        else:
            if num==0:
                num=11
            l=distance(nowL,num)
            r=distance(nowR,num)
            if l>r:
                answer+='R'
                nowR=num
            elif r>l:
                answer+='L'
                nowL=num
            else:
                if isHand:
                    answer+='L'
                    nowL=num
                else:
                    answer+='R'
                    nowR=num
                
    return answer
