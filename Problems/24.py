# 안테나
# https://www.acmicpc.net/problem/18310

import sys

n = int(input())
house = list(map(int, sys.stdin.readline().split()))
house.sort()

# 중간값(median)을 출력
print(house[(n - 1) // 2])