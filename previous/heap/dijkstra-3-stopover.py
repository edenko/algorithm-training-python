# 5 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 5 5
# 4 5 2
# 2 3

## 9

# 필수 경유지 최단 경로 문제
# 노드 1에서 출발하여 두 개의 특정 노드 v1, v2를 반드시 모두 지나
# 마지막 노드 N까지 가는 최단 거리를 구하라.

# 조건
# 양방향 그래프
# 간선 비용 W ≥ 1
# 다익스트라 사용
# 도달 불가능한 경우 -1 출력

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
    graph[b].append((a, w))


# v1, v2 입력받기
v1, v2 = map(int, input().split())

# 다익스트라 3번 호출
dist = dijkstra(1, graph, n)
distV1 = dijkstra(v1, graph, n)
distV2 = dijkstra(v2, graph, n)

# route1, route2 계산
route1 = dist[v1] + distV1[v2] + distV2[n]
route2 = dist[v2] + distV2[v1] + distV1[n]

# INF 체크 후 결과 출력
answer = min(route1, route2)
print(answer if answer < INF else -1)
