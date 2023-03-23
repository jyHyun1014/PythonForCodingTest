# 피보나치 함수 소스코드

# 피보나치 함수(Fibonacci Fuction)를 재귀 함수로 구현
# n이 커지면 수행 시간이 기하급수적으로 늘어남
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))