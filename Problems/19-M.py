# 연산자 끼워 넣기
# https://www.acmicpc.net/problem/14888

from itertools import permutations

n = int(input())
array = list(map(int, input().split()))
data = list(map(int, input().split()))
operator = []
operator.extend([0] * data[0])
operator.extend([1] * data[1])
operator.extend([2] * data[2])
operator.extend([3] * data[3])
nPr = list(permutations(operator, len(operator)))
nPr = list(set(nPr))
answer = []
for op in nPr:
    result = array[0]
    for i in range(len(op)):
        if op[i] == 0:
            result += array[i+1]
        elif op[i] == 1:
            result -= array[i+1]
        elif op[i] == 2:
            result *= array[i+1]
        else:
            if result > 0:
                result //= array[i+1]
            else:
                result = (-result) // array[i + 1]
                result = -result
    answer.append(result)

print(max(answer))
print(min(answer))