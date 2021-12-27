def gcd(a,b):
    while b>0:
        a,b=b,a%b #유클리드호제법
    return a

def solution(arr):
    answer = 0
    if len(arr)==1:
        return arr[0]
    
    lcm=arr[0]
    #두개씩 최소공배수를 구함
    for i in range(1,len(arr)):
        lcm=(lcm*arr[i])//gcd(lcm,arr[i])
    answer=lcm
    return answer
