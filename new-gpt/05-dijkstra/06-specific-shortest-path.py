# 백준 1504번 — 특정한 최단 경로

# 1번부터 N번까지 정점이 있는 그래프가 있어.
# 목표는 1번 정점에서 출발해 N번 정점까지 가는 최단 거리를 구하는 거야.
# 그런데 추가 조건이 있어.
# 주어진 두 정점 v1, v2를 반드시 모두 지나가야 해.

# 중요한 조건은 다음과 같아.
# - 그래프는 양방향이야.
# - 간선마다 이동 비용이 있어.
# - v1, v2를 모두 거쳐야 해.
# - 정점이나 간선을 다시 지나가도 돼.
# - 조건을 만족하는 경로가 없다면 -1을 출력해야 해.

# 정점 N, 간선 M
# 비용 M개
# v1,v2

# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3

# 7

# 4 2
# 1 2 1
# 3 4 1
# 2 3

# -1

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))
  graph[b].append((a, w))

lv1, lv2 = map(int, input().split())
INF = float('inf')

def dijkstra(start):
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

  return dist

path = dijkstra(1)
path_v1 = dijkstra(lv1)
path_v2 = dijkstra(lv2)

route1 = path[lv1] + path_v1[lv2] + path_v2[n]
route2 = path[lv2] + path_v2[lv1] + path_v1[n]
result = min(route1, route2)
print(-1 if result == INF else result)
