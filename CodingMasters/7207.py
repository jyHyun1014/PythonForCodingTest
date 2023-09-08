# 7207 파스칼 피라미드
# 시뮬레이션

import copy
n = int(input())

data = [[0] * n for _ in range(n)]
data[0][0] = 1

new = []
for k in range(1, n):
    new = copy.deepcopy(data)
    for i in range(n):
        for j in range(n):
            if i + j <= k:
                new[i][j] = data[i][j]
                if 0 <= i-1:
                    new[i][j] += data[i-1][j]
                if 0 <= j-1:
                    new[i][j] += data[i][j-1]
    data = copy.deepcopy(new)
    
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            print(data[i][j], end=' ')
    print()
