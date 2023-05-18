# 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    stages.sort()
    result = []

    for x in range(N):
        # x+1번 스테이지 실패한 사용자들의 인덱스
        fail_users = [i for i, value in enumerate(stages) if value == x + 1]
        if fail_users == [] or len(stages) - fail_users[0] == 0:
            result.append((x + 1, 0))
        else:
            failure_rate = len(fail_users) / (len(stages) - fail_users[0])
            result.append((x + 1, failure_rate))

    result.sort(key=lambda k: (-k[1], k[0]))
    answer = []
    for i, j in result:
        answer.append(i)
    return answer