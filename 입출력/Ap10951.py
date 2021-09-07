import sys

lines = sys.stdin.readlines() #파일 끝 부분까지 한번에 가져옴
for line in lines:
    a,b = map(int, line.split())
    print(a+b)
