import sys

n=int(sys.stdin.readline())
dic={}

for i in range(n):
    temp=int(sys.stdin.readline())
    if temp in dic:
        dic[temp]+=1
    else:
        dic[temp]=1
#딕셔너리.items => 딕셔너리의 (key,value)를 list(dict_items)객체로 반환 
dic=sorted(dic.items(), key=lambda x:(-x[1],x[0]))
print(dic[0][0])
