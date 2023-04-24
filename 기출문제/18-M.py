# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def recursive(w):
    # 1 : 빈 문자열일 경우, 반환
    if w == '':
        return w
    # 2 u, v로 분리
    count_left = 0
    count_right = 0
    for i in range(len(w)):
        if w[i] == '(':
            count_left += 1
        elif w[i] == ')':
            count_right += 1
        if count_left == count_right:
            u = w[0:i + 1]
            v = w[i + 1:len(w)]
            break
            # u가 '올바은 괄호 문자열'인지 아닌지 검사
    now_u = u
    for i in range(count_left):
        now_u = now_u.replace('()', '')
    if now_u == '':  # 올바은 괄호 문자열
        # 3 u가 '올바은 괄호 문자열이라면' v에 대해 recursive 수행
        v = recursive(v)
        return u + v  # 3-1
    else:  # 올바른 괄호 문자열이 아님
        # 4
        empty_str = '('  # 4-1
        v = recursive(v)  # 4-2
        empty_str = empty_str + v + ')'  # 4-2, 4-3
        u = u[1:len(u) - 1]  # 4-4
        u = u.translate(u.maketrans({  # 4-4
            ')': '(',
            '(': ')'
        }))
        empty_str = empty_str + u  # 4-4
        return empty_str  # 4-5


def solution(p):
    answer = ''
    answer = recursive(p)

    return answer