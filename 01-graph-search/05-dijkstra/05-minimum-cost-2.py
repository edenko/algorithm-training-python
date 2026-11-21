# 백준 11779번 — 최소비용 구하기 2

# N개의 도시와 M개의 버스가 있어.
# 버스마다 출발 도시, 도착 도시, 비용이 정해져 있고, 버스는 방향이 있는 간선이야.
# 출발 도시에서 도착 도시까지 최소 비용으로 이동하는 경로를 찾아야 해.

# 출력해야 하는 건 세 가지야.
# 1. 최소 비용
# 2. 최소 비용으로 이동하는 경로에 포함된 도시의 개수
# 3. 실제로 이동한 도시 번호를 출발지부터 도착지 순서로 출력

# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

# 4
# 3
# 1 3 5 or 1 4 5

import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))

start, end = map(int, input().split())
INF = float('inf')
dist = [INF] * (n + 1)
dist[start] = 0
parent = [-1] * (n + 1)

heap = []
heapq.heappush(heap, (0, start))

while heap:
  cost, node = heapq.heappop(heap)

  if cost > dist[node]:
    continue

  for next_node, weight in graph[node]:
    new_cost = cost + weight

    if new_cost < dist[next_node]:
      dist[next_node] = new_cost
      parent[next_node] = node
      heapq.heappush(heap, (new_cost, next_node))

print(dist[end])

path = [end]
node = end
while True:
  if node == start:
    break

  ari = parent[node]
  path.append(ari)
  node = ari

print(len(path))
print(*reversed(path))
