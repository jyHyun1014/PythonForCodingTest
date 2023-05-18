# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(array):
    n = len(array) # 행렬의 크기
    result = [[0] * n for _ in range(n)]  # 결과를 넣을 리스트
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = array[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(array):
    length = len(array) // 3
    for i in range(length, 2 * length):
        for j in range(length, 2 * length):
            if array[i][j] != 1:
                return False
    return True
def solution(key, lock):
    n = len(lock)  # 자물쇠 크기 N
    m = len(key)  # 열쇠 크기 M
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)   # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False