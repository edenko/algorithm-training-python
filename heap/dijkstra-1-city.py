# 최소시간 이동 (그래프 기본형)

# 도시가 N개 있고, 도로가 M개 있다.
# 각 도로는 A → B 로 이동할 때 시간이 T만큼 걸린다.

# 도시 1번에서 N번 도시까지 이동하는 데 걸리는 최소 시간을 구하라.

# 5 6
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 4 5 1

## 8

# 최소시간 이동 (그래프 기본형)

# 도시가 N개 있고, 도로가 M개 있다.
# 각 도로는 A → B 로 이동할 때 시간이 T만큼 걸린다.

# 도시 1번에서 N번 도시까지 이동하는 데 걸리는 최소 시간을 구하라.

import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for nx, t in graph[now]:
            new_cost = cost + t
            if new_cost < dist[nx]:
                dist[nx] = new_cost
                heapq.heappush(pq, (new_cost, nx))

    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

start = 1
dist = dijkstra(start, graph, n)

print(-1 if dist[n] == INF else dist[n]) 
