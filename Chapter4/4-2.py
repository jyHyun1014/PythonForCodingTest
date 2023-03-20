# 시각

# 입력 예시
# 5

# N을 입력 받기
n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)