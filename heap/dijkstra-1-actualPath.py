import sys, heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    parent = [-1] * (n + 1)
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
                parent[nx] = now
                heapq.heappush(pq, (new_cost, nx))

    return dist, parent

def restore_path(parent, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())
dist, parent = dijkstra(start, graph, n)

print(dist[end])
print(*restore_path(parent, end))

# 5 6
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 4 5 1
# 1 5

# 8
# 1 2 4 5
