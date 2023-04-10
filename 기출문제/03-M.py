# 문자열 뒤집기
# https://www.acmicpc.net/problem/1439

data = input()

zero = 0
one = 0
before = 2

for i in data:
    if before != 0 and i == '0':
        zero += 1
        before = 0
    elif before != 1 and i == '1':
        one += 1
        before = 1

print(min(zero, one))