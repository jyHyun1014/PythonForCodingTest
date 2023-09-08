# 7255 영양점수
# 완전탐색

from itertools import permutations, combinations
n = int(input())
ingredient = range(n)
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

candidates = list(combinations(ingredient, int(n/2)))
answer = float('inf')

for food1 in candidates:
    food2 = [i for i in ingredient if i not in food1]  # food1에 포함되지 않은 식재료 저장
    
    combo1 = list(permutations(food1, 2))
    combo2 = list(permutations(food2, 2))
    score1 = 0
    score2 = 0
    
    for x, y in combo1:
        score1 += data[x][y]
    for x, y in combo2:
        score2 += data[x][y]
           
    answer = min(abs(score1-score2), answer)
print(answer)