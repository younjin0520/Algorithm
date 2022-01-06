import sys

string=sys.stdin.readline().strip()
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
idx=0
result=0
while idx<len(string):
    if idx+2<=len(string) and string[idx:idx+2] in alpha:
        result+=1
        idx+=2
    elif idx+3<=len(string) and string[idx:idx+3] in alpha:
        result+=1
        idx+=3
    else:
        result+=1
        idx+=1
print(result)
