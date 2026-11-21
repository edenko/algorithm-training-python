# 백준 1238번 — 파티

# 1번부터 N번까지 번호가 붙은 마을이 있어.
# 각 마을에는 학생이 한 명씩 살고 있고, 모든 학생이 X번 마을에서 열리는 파티에 참석하려고 해.
# 파티에 갔다가 다시 자기 마을로 돌아와야 해.
# 각 학생이 최단 경로로 왕복한다고 할 때, 왕복 시간이 가장 오래 걸리는 학생의 시간을 출력해.

# 중요한 조건이 있어.
# - 도로는 방향이 있는 간선이야.
# - 도로마다 이동 시간이 다를 수 있어.
# - 갈 때와 돌아올 때의 최단 시간이 서로 다를 수 있어.
# - 왕복 시간은 집 → X의 최소 시간 + X → 집의 최소 시간이야.
# 입력 범위는 1 ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000이고, 도로 이동 시간은 양의 정수야.

# 마을, 도로, 파티가 열리는 마을

# 4 8 2
# 1 2 4
# 1 3 2
# 1 4 7
# 2 1 1
# 2 3 5
# 3 1 2
# 3 4 4
# 4 2 3

# 10

import heapq

n, m, party = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph1 = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, w = map(int, input().split())
  graph[a].append((b, w))
  graph1[b].append((a, w))

INF = float('inf')

def dijkstra(start, graph):
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

dist_from_party = dijkstra(party, graph)
dist_to_party = dijkstra(party, graph1)
result = 0
for i in range(1, n + 1):
  result = max(result, dist_from_party[i] + dist_to_party[i])

print(result)