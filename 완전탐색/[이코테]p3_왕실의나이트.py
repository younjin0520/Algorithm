#구현_왕실의 나이트
x,y=map(str,input())
x=ord(x)-97
y=int(y)-1
result=0

#수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#오른쪽이동
if x+2<8:
    if y+1<8:
        result+=1
    if y-1>=0:
        result+=1
if x-2>=0:
    if y+1<8:
        result+=1
    if y-1>=0:
        result+=1        
#수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
if y+2<8:
    if x+1<8:
        result+=1
    if x-1>=0:
        result+=1
if y-2>=0:
    if x+1<8:
        result+=1
    if x-1>=0:
        result+=1

print(result)
