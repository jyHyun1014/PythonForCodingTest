# 연구소
# https://www.acmicpc.net/problem/14502

from itertools import combinations
import copy

# 연구소의 크기 N x M
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


virus = []  # 초기에 바이러스가 있는 위치
blank = []  # 초기에 빈칸의 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

# 바이러스 퍼트리기
def dfs(x, y, new_graph):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if new_graph[x][y] == 0:
        new_graph[x][y] = 2
        dfs(x - 1, y, new_graph)
        dfs(x, y - 1, new_graph)
        dfs(x + 1, y, new_graph)
        dfs(x, y + 1, new_graph)

result = 0  # 안전 영역 크기 (맵에서 0의 개수)
candidates = list(combinations(blank, 3))   # 벽을 설치할 수 있는 위치의 모든 경우의 수

# 모든 후보군에 대해 벽을 설치해보기
for a, b, c in candidates:
    new_graph = copy.deepcopy(graph)    # 중요!!!!!
    new_graph[a[0]][a[1]] = 1
    new_graph[b[0]][b[1]] = 1
    new_graph[c[0]][c[1]] = 1
    count = 0
    # 초기 바이러스 위치를 기반으로 바이러스 퍼트리기
    for v in virus:
        dfs(v[0] - 1, v[1], new_graph)
        dfs(v[0], v[1] - 1, new_graph)
        dfs(v[0] + 1, v[1], new_graph)
        dfs(v[0], v[1] + 1, new_graph)
    # 초기 빈칸의 위치를 기반으로 안전 영역의 개수 계산하기
    for i in blank:
        if new_graph[i[0]][i[1]] == 0:
            count += 1
    result = max(result, count)

print(result)