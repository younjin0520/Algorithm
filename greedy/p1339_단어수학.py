#단어를 숫자로 바꿔서 계산

import sys

N=int(sys.stdin.readline())
words=[]
dic={}
num=9
result=0
        
for i in range(N):
    inputWord=sys.stdin.readline().strip()
    words.append(inputWord.zfill(8)) #8자리로 자릿수 맞추기

for word in words:
    for i in range(len(word)):
        if word[i]=='0':
            continue
        if word[i] in dic:
            dic[word[i]]+=10**(len(word)-1-i)
        else:
            dic[word[i]]=10**(len(word)-1-i)

dic=sorted(dic.items(),key=lambda x: -x[1]) #딕셔너리 value값으로 정렬하기 - list형태로 반환
dic=dict(dic)

for key in dic.keys():
    dic[key]=num
    num-=1

for i in range(len(words)):
    tmp=''
    for j in range(len(words[i])):
        if words[i][j]=='0':
            continue
        tmp+=str(dic[words[i][j]])
    result+=int(tmp)

print(result)
