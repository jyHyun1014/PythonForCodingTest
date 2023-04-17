# 뱀
# https://www.acmicpc.net/problem/3190

from collections import deque

n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수

board = [[0] * (n + 2) for _ in range(n + 2)]   # 보드판 0:갈 수 있는 길 1:벽 또는 뱀의 몸 2:사과
for i in range(n):  # 보드판 테두리 1로 색칠하기(벽)
    board[0][i] = 1
    board[-1][i] = 1
    board[i][0] = 1
    board[i][-1] = 1

# 사과의 위치 입력받기
for _ in range(k):
    x, y = map(int, input().split())    # 사과의 위치 좌표
    board[x][y] = 2

# 방향 변환 정보 입력받기
l = int(input())    # 방향 변환 횟수
way = []            # 방향 변환 리스트
count_way = 0       # way 리스트에 순차적으로 접근할 인덱스
for _ in range(l):
    x, c = input().split()  # x초가 끝난 뒤에 c방향으로 회전
    way.append((int(x), c))

x, y = 1, 1 # 뱀의 머리(시작 위치)
s = 0   # 초 시간
direction = 0   # 0:오른쪽 1:아래쪽 2:왼쪽 3:위쪽

def change_direction(c):
    global direction
    if c == 'L':
        direction -= 1
    else:
        direction += 1
    if direction == -1:
        direction = 3
    elif direction == 4:
        direction = 0

queue = deque()
queue.append((x, y))    # 시작 위치 큐에 넣기
board[x][y] = 1 # 시작 위치에 뱀 놓기

while True:
    s += 1  # 초

    # 뱀의 머리 움직이기
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x -= 1

    # 뱀의 머리가 어디로 갔는지 검사
    if board[x][y] == 1:    # 벽 또는 몸통에 부딪힌 경우
        print(s)
        break  # 게임 종료
    elif board[x][y] == 2:  # 사과가 있는 경우
        queue.append((x, y))
        board[x][y] = 1
    else:                   # board[x][y] = 0 인 경우
        queue.append((x, y))
        board[x][y] = 1
        a, b = queue.popleft()
        board[a][b] = 0

    # 방향 변환 할지 확인
    if count_way < l and way[count_way][0] == s:
        change_direction(way[count_way][1])
        count_way += 1