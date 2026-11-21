# 4 5
# 1 2 1
# 1 3 1
# 2 4 1
# 3 4 1
# 1 4 3

## 2 2

# 최단 거리 + 최단 경로 개수 구하기

# N개의 노드와 M개의 간선이 있다.
# 각 간선은 A → B 로 이동할 때 비용 W가 든다.
# 1번에서 N번까지 갈 수 있는 최단 거리와,
# 그 최단 거리로 갈 수 있는 서로 다른 경로의 개수를 구하라.

# 경로 수가 매우 클 수 있으므로
# 1,000,000,007 (10^9+7) 로 나눈 값을 출력한다.

import sys, heapq
input = sys.stdin.readline
INF = float('inf')
MOD = 1000000007

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0

    count = [0] * (n + 1)
    count[start] = 1

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cost, now = heapq.heappop(pq)

        if cost > dist[now]:
            continue

        for nx, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nx]:
                dist[nx] = new_cost
                count[nx] = count[now]
                heapq.heappush(pq, (new_cost, nx))
            elif new_cost == dist[nx]:
                count[nx] += count[now]
                count[nx] %= MOD

    return dist, count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start = 1
dist, count = dijkstra(start, graph, n)

print(dist[n], count[n])
