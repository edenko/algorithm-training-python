import heapq, sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0

    # 우선순위 큐/힙
    pq = []
    heapq.heappush(pq, (0, start)) # 힙에는 항상 (거리, 노드) 순서로 넣음

    while pq:
        cost, now = heapq.heappop(pq) # now - 현재까지 가장 짧은 경로가 확정된 노드

        if cost > dist[now]: # cost가 dist[now]보다 크면 이미 더 좋은 경로가 처리됨 -> continue
            continue

        for nx, w in graph[now]: # 현재 노드에서 갈 수 있는 모든 노드 탐색
            new_cost = cost + w

            if new_cost < dist[nx]: # 더 짧은 거리 발견 -> pq 갱신
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

for i in range(1, n + 1):
    print("INF" if dist[i] == INF else dist[i])

# 5 6
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 4 5 1
# 1

# 0
# 2
# 3
# 7
# 8