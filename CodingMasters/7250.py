# 7250 어묵과 파르페

import sys

s = list(sys.stdin.readline())
data =[] # 묶어서 개수 세기. 어묵은 무조건 0으로 넣기
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        if s[i] == 'F':
            data.append(0)
        else:
            data.append(count)
        count = 1

print(sum(data)-max(data))  # 제일 큰 뭉텅이 빼고 나머지 더하면 됨