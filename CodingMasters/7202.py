# 7202 신입사원 채용

import sys
input = sys.stdin.readline

n = int(input())
score = []
for i in range(n):
    a, b = map(int, input().split())
    score.append((a, b, i)) # (서류점수, 면접점수, 지원자인덱스) 를 리스트에 저장 
    
score1 = sorted(score, reverse=True, key=lambda x: (x[0], x[1]))  # 서류점수, 면접점수 기준으로 내림차순 정렬 
score2 = sorted(score, reverse=True, key=lambda x: (x[1], x[0]))  # 면접점수, 서류점수 기준으로 내림차순 정렬

print(score1)
print(score2)
# print(score)
temp = set()        # 임시 저장소 # 집합을 사용하는 이유는 새로운 원소 추가, 특정한 값을 갖는 원소 삭제의 시간 복잡도 O(1)
rank = 1            # 순위
answer = [0] * n    # 지원자들의 순위 리스트
for i in range(n): 
    if score1[i][2] not in temp:    # (서류점수 순서) 임시저장소에 지원자가 없다면 임시저장소에 지원자 추가
        temp.add(score1[i][2])
    else:                           # (서류점수 순서) 임시저장소에 지원자가 있다면 임시저장소에서 지원자 삭제
        temp.remove(score1[i][2])
        answer[score1[i][2]] = rank
    if score2[i][2] not in temp:    # (면접점수 순서) 임시저장소에 지원자가 없다면 임시저장소에 지원자 추가
        temp.add(score2[i][2])
    else:                           # (면접점수 순서) 임시저장소에 지원자가 있다면 임시저장소에서 지원자 삭제
        temp.remove(score2[i][2])
        answer[score2[i][2]] = rank
    # print(temp)
    if len(temp) == 0:              # 임시저장소가 비어있다면, 순위 넣어주기
        rank = i+2

for i in range(n):
    print(answer[i], end = ' ')
    
#            C          A         B         E        D
# 서류순 [(71, 56), (68, 73), (56, 64), (18, 22), (15, 23)]
# 면접순 [(68, 73), (56, 64), (71, 56), (15, 23), (18, 22)]
#           A           B         C         D       E
#           1           1         1         4       4