# 백준 1916번 — 최소비용 구하기

# N개의 도시가 있고, 도시 사이를 이동하는 M개의 버스가 있어.
# 버스마다 출발 도시, 도착 도시, 이동 비용이 주어져.

# 출발 도시에서 도착 도시까지 이동하는 데 필요한 최소 비용을 구하는 것이야.

# 조건은 다음과 같아.
# - 도시는 1번부터 N번까지 있어.
# - 버스는 정해진 방향으로만 이동할 수 있어.
# - 같은 출발 도시와 도착 도시를 연결하는 버스가 여러 개 있을 수도 있어.
# - 출발 도시에서 도착 도시까지 이동할 수 있는 경우만 주어져.

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
      heapq.heappush(heap, (new_cost, next_node))

print(dist[end])