# 기둥과 보 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

def pillar_check(x, y):
    # 바닥 위에 있거나 / 보의 한쪽 끝부분 위에 있거나 / 다른 기둥 위에 있는지 확인
    if y == 0 or [x - 1, y, 1] in result or [x, y, 1] in result or [x, y - 1, 0] in result:
        return True
    else:
        return False

def beam_check(x, y):
    # 한쪽 끝부분이 기둥 위에 있거나 / 양쪽 끝부분이 다른 보와 동시에 연결되어 있는지 확인
    if [x, y - 1, 0] in result or [x + 1, y - 1, 0] in result or ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
        return True
    else:
        return False

# 기둥 만들기
def pillar_make(x, y):
    if pillar_check(x, y):
        result.append([x, y, 0])

# 보 만들기
def beam_make(x, y):
    if beam_check(x, y):
        result.append([x, y, 1])

# 보 삭제하기
def beam_delete(x, y):
    result.remove([x, y, 1])    # 일단 삭제하고 나머지가 조건을 만족하는지 확인
    if [x, y, 0] in result and not pillar_check(x, y):  # 왼쪽 위에 기둥이 있는 경우
        result.append([x, y, 1])
        return
    if [x + 1, y, 0] in result and not pillar_check(x + 1, y):  # 오른쪽 위에 기둥이 있는 경우
        result.append([x, y, 1])
        return
    if [x - 1, y, 1] in result and not beam_check(x - 1, y):    # 왼쪽에 보가 있는 경우
        result.append([x, y, 1])
        return
    if [x + 1, y, 1] in result and not beam_check(x + 1, y):    # 오른쪽에 보가 있는 경우
        result.append([x, y, 1])

# 기둥 삭제하기
def pillar_delete(x, y):
    result.remove([x, y, 0])    # 일단 삭제하고 나머지가 조건을 만족하는지 확인
    if [x, y + 1, 0] in result and not pillar_check(x, y + 1):  # 위에 기둥이 있는 경우
        result.append([x, y, 0])
        return
    if [x - 1, y + 1, 1] in result and not beam_check(x - 1, y + 1):    # 왼쪽 위에 보가 있는 경우
        print("1번")
        result.append([x, y, 0])
        return
    if [x, y + 1, 1] in result and not beam_check(x, y + 1):    # 오른쪽 위에 보가 있는 경우
        print("2qjs")
        result.append([x, y, 0])

def solution(n, build_frame):
    global result
    result = []

    for build in build_frame:
        if build[2] == 0 and build[3] == 0:
            pillar_delete(build[0], build[1])
        elif build[2] == 0 and build[3] == 1:
            pillar_make(build[0], build[1])
        elif build[2] == 1 and build[3] == 0:
            beam_delete(build[0], build[1])
        elif build[2] == 1 and build[3] == 1:
            beam_make(build[0], build[1])

    result.sort()
    return result