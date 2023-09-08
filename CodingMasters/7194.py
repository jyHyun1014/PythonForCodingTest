# 7194 분리수거장
# 완전탐색

import sys
input = sys.stdin.readline

# 아파트 단지 수
n = int(input())
data = []
for i in range(n):
    d, a = map(int, input().split())
    data.append((d, a))
    
total_min = float('inf') # 각 주민 거리 합 최소

for i in range(n):
    total = 0
    for j in range(n):
        total += abs(data[i][0] - data[j][0]) * data[j][1]
    if total_min > total:
        total_min = total
        answer = i+1 # 단지 번호
        
print(answer)