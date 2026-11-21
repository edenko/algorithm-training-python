# 백준 1753번 최단경로

# 4 5
# 1
# 1 2 2
# 1 3 5
# 2 3 1
# 2 4 4
# 3 4 2

# 0
# 2
# 3
# 5

import heapq

n, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(e):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))

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

for d in dist[1:]:
  if d == INF:
    print('INF')
  else:
    print(d)
