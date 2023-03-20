# 2가지 방식으로 구현한 팩토리얼 예제

# 반복문으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀함수로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 코드 그대로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복문으로 구현:', factorial_iterative(5))
print('재귀함수로 구현:', factorial_recursive(5))