import sys

s=list(sys.stdin.readline())

for i in range(len(s)-1):
    if s[i].isalpha():
        if ord(s[i])<97:#대문자
            if ord(s[i])+13<91:
                s[i]=chr(ord(s[i])+13)
            else:
                s[i]=chr(ord(s[i])-13)
        else:#대문자
            if ord(s[i])+13<123:
                s[i]=chr(ord(s[i])+13)
            else:
                s[i]=chr(ord(s[i])-13)

for word in s:
    print(word,end='')
