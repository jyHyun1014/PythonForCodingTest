# 재귀 함수 예제

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 함수를 무한히 호출하기 때문에 오류가 난다.