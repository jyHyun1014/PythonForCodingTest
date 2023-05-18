# 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(len(dp[i])):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == len(dp[i]) - 1:
            right_up = 0
        else:
            right_up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(left_up, right_up)

print(max(dp[n - 1]))