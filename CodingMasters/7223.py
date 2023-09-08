# 7223 떡 하나 주면 안 잡아먹지
# 다익스트라 최단경로

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
result = [[INF] * n for _ in range(n)]   # 최단 경로 테이블
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 이동할 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0     # 시작 위치는 (0, 0)
# 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
q = [(graph[x][y], x, y)]
result[x][y] = graph[x][y]

# 다익스트라 알고리즘
while q:
    dist, x, y = heapq.heappop(q)   # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
    
    if result[x][y] < dist:         # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        continue
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cost = dist + graph[nx][ny]
            if cost < result[nx][ny]:
                result[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
            
print(result[n-1][n-1])