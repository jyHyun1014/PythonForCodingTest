# 행성 터널
# https://www.acmicpc.net/problem/2887

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 입력받기
n = int(input())
parent = [0] * n    # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# 모든 노드와 간선을 담을 리스트
nodes = []
edges = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(n):
    x, y, z = map(int, input().split())
    nodes.append((x, y, z, i))

# x에 대해 정렬
nodes.sort()
for i in range(n - 1):
    cost = min(abs(nodes[i][0] - nodes[i + 1][0]), abs(nodes[i][1] - nodes[i + 1][1]), abs(nodes[i][2] - nodes[i + 1][2]))
    edges.append((cost, nodes[i][3], nodes[i + 1][3]))

# y에 대해 정렬
nodes.sort(key=lambda x: x[1])
for i in range(n - 1):
    cost = min(abs(nodes[i][0] - nodes[i + 1][0]), abs(nodes[i][1] - nodes[i + 1][1]), abs(nodes[i][2] - nodes[i + 1][2]))
    edges.append((cost, nodes[i][3], nodes[i + 1][3]))

# z에 대해 정렬
nodes.sort(key=lambda x: x[2])
for i in range(n - 1):
    cost = min(abs(nodes[i][0] - nodes[i + 1][0]), abs(nodes[i][1] - nodes[i + 1][1]), abs(nodes[i][2] - nodes[i + 1][2]))
    edges.append((cost, nodes[i][3], nodes[i + 1][3]))

# 간선을 비용 순으로 정렬
edges.sort()
answer = 0

# 간선을 하나씩 확인하며
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)