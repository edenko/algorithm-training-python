import heapq, sys

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

        for nx, w in graph[now]:
            new_cost = cost + w

            if new_cost < dist[nx]:
                dist[nx] = new_cost
                heapq.heappush(pq, (new_cost, nx))

    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start = int(input())

dist = dijkstra(start, graph, n)
