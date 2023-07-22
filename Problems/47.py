# 청소년 상어
# https://www.acmicpc.net/problem/19236

import sys
input = sys.stdin.readline
import copy

# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 같은 방향 값을 담는 테이블
graph = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        graph[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(graph, index):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == index:
                return (i, j)
    return None

# 모든 물고기 회전 및 이동시키는 함수
def move_all_fishes(graph, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 낮은 번호부터 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(graph, i)
        if position != None:
            x, y = position[0], position[1]
            direction = graph[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면
                if 0 <= nx < 4 and 0 <= ny < 4 and not(nx == now_x and ny == now_y):
                    graph[x][y][1] = direction
                    graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                    break
                direction = turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(graph, now_x, now_y):
    positions = []
    direction = graph[now_x][now_y][1]
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않고 물고기가 존재하는 경우
        if 0 <= now_x < 4 and 0 <= now_y < 4 and graph[now_x][now_y][0] != -1:
            positions.append((now_x, now_y))
    return positions

result = 0  # 최종 결과

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(graph, now_x, now_y, total):
    global result
    graph = copy.deepcopy(graph)    # 리스트를 통째로 복사

    total += graph[now_x][now_y][0] # 현재 위치의 물고기 먹기
    graph[now_x][now_y][0] = -1        # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(graph, now_x, now_y)    # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(graph, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(graph, next_x, next_y, total)

# 청소년 상어 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(graph, 0, 0, 0)
print(result)