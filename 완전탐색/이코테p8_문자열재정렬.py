#문자열 재정렬
import sys

string=list(sys.stdin.readline().strip())
string.sort()
result=0
for i in range(len(string)):
    if string[i].isdigit():
        result+=int(string[i])
    else:
        break
string=string[i:]
print(''.join(string)+str(result))
