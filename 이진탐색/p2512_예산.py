import sys
N=int(sys.stdin.readline())
prices=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())

def cal(num):
    result=0
    for price in prices:
        if price>num:
            result+=num
        else:
            result+=price
    return result

start=0
end=max(prices)

while start<=end:
    mid=(start+end)//2
    result=cal(mid)
    #돈을 초과했을 때
    if result>M:
        end=mid-1
    else:
        start=mid+1
print(end)
        
        
