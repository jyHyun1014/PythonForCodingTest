# 7254 탈출사건
# dfs

n, m = map(int, input().split())
graph = []
new = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
     
# 빈칸 재류어로 채우기
def spread(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and new[nx][ny] == 0:
            new[nx][ny] = 2
            spread(nx, ny)

# 빈칸 개수 세기
def count_safe():
    total = 0
    for i in range(n):
        for j in range(m):
            if new[i][j] == 0:
                total += 1
    return total

def dfs(count):
    global answer
    # 울타리 3개 설치 완료 했다면
    if count == 3:
        for i in range(n):
            for j in range(m):
                new[i][j] = graph[i][j]
        
        for i in range(n):
            for j in range(m):
                if new[i][j] == 2:
                    spread(i, j)
        answer = max(answer, count_safe())
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1
                    
dfs(0)
print(answer)