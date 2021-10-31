#풀이방법: 각 숫자가 나온 개수만큼 체크하고 가장 많이 나온것부터 한개 나온것까지 차례로 씀
def solution(s):
    arr=[0]*100001
    tmp=''
    answer=[]
    for i in s:
        if i.isdigit():
            tmp+=i
        else:
            if len(tmp)>0:
                arr[int(tmp)]+=1
                tmp=''
    length=max(arr)
    for i in range(length,0,-1):
        answer.append(arr.index(i))
    return answer
