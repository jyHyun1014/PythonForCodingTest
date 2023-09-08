# 7218 약육강식
# DP

import sys
input = sys.stdin.readline

n = int(input())
shark = list(map(int, input().split()))
eat = [0] * n  # 먹은 상어의 수 저장하는 리스트

for i in range(n):
    for j in range(i):
        if shark[j] < shark[i]:  # 내 앞에 작은 상어가 나타나면,
            eat[i] = max(eat[i], eat[j] + 1)  # 앞에서 내가 먹었던 상어 수 최대 vs 작은 상어가 먹은 수 + 1
            # eat[i] = eat[j] + 1   ## 1 2 3 4 1 3 8 실패
    
print(max(eat) + 1) # 나 자신도 관계에 포함