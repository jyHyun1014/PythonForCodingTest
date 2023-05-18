# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

from collections import deque

def solution(s):
    answer = len(s)  # 정답(압축해서 표현한 문자열 중 가장 짧은 것의 길이)

    count = 0       # 중복될 때마다 카운트
    queue = deque() # 카운트 저장

    for i in range(1, (len(s) // 2) + 1):
        for j in range(0, len(s) - i, i):
            if s[j:j + i] == s[j + i:j + i + i]:
                count += 1
            else:  # 중복이 끝났을 때
                if count > 0:
                    queue.append(count)
                    count = 0  # 초기화
        if count > 0:
            queue.append(count)
            count = 0  # 초기화

        alphabet = 0    # 중복된 알파벳 총 개수
        num = 0         # 압축된 문자열에 들어갈 수의 총 개수

        while queue:
            x = queue.popleft()
            alphabet += x * i
            num += len(str(x+1))  # 압축 문자열에는 x+1로 표현 해야함

        answer = min(answer, (len(s) - alphabet) + num) # 가장 짧은 것 선택

    return answer