# 빠르게 입력받기
# sys 라이브러리 readline()

import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()  # rstrip() 엔터공백문자 제거
# 입력받은 문자열 그대로 출력
print(input_data)

# 한 줄에 여러 수 입력 받기
f = sys.stdin.readline
a, b = map(int, f().split())
print(a, b)