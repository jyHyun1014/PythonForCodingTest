# 럭키 스트레이트
# https://www.acmicpc.net/problem/18406

n = input()

sum1 = 0    # 왼쪽 부분의 자릿수 합
sum2 = 0    # 오른쪽 부분의 자릿수 합

for i in range(len(n)//2):
    sum1 += int(n[i])
    sum2 += int(n[(-i) - 1])

# 왼쪽과 오른쪽 부분의 자릿수 합이 동일한지 검사
if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
