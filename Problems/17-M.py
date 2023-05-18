# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

# 나의 틀린 답안
# 초마다 모든 바이러스가 우선순위 따라 동시에 퍼져야 하는데
# 이 코드는 1번 바이러스를 s초까지 퍼트리고, 2번 바이러스를 s초까지 퍼트리는 것을 반복하기 때문에 틀림

import sys

n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data)
    for j in range(n):
        if data[j] != 0:
            virus.append((i, j, data[j]))
s, x, y = map(int, input().split())

virus.sort(key = lambda x:x[2])

def dfs(x, y, virus_num, s_count):
    if x <= -1 or x >= n or y <= -1 or y >= n or s_count == s:
        return
    if graph[x][y] == 0:
        graph[x][y] = virus_num
        dfs(x - 1, y, virus_num, s_count + 1)
        dfs(x, y - 1, virus_num, s_count + 1)
        dfs(x + 1, y, virus_num, s_count + 1)
        dfs(x, y + 1, virus_num, s_count + 1)

for i, j, v in virus:
    dfs(i - 1, j, v, 0)
    dfs(i, j - 1, v, 0)
    dfs(i + 1, j, v, 0)
    dfs(i, j + 1, v, 0)

# print(graph)
print(graph[x - 1][y - 1])