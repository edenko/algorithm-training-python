# 2D Grid 최단 경로 복원

# N × N 크기의 그리드가 있다.
# 각 칸마다 이동하는 데 드는 비용이 주어진다.

# 당신은 항상 (0, 0) 위치(왼쪽 위)에서 시작하고
# ( N-1, N-1 ) 위치(오른쪽 아래)로 이동하려 한다.

# 이동은 상하좌우로만 가능하며,
# 각 칸의 비용만큼 누적 비용이 증가한다.

# 다익스트라 알고리즘을 사용하여
# 1. 최소 이동 비용
# 2. 그 비용으로 도착하는 경로 (0,0 → N-1,N-1) 
# 을 출력하라.
# 경로는 이동하는 칸의 좌표를 순서대로 출력한다.

# 3
# 5 5 4
# 3 9 1
# 3 2 7

# 20
# (0,0) (1,0) (2,0) (2,1) (2,2)

import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(x, y, grid, n):
    dist = [[INF] * n for _ in range(n)]
    dist[y][x] = grid[y][x]
    parent = [[(-1, -1)] * n for _ in range(n)]
    pq = []
    heapq.heappush(pq, (grid[y][x], x, y))

    while pq:
        cost, cx, cy = heapq.heappop(pq)

        if cost > dist[cy][cx]:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + grid[ny][nx]
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    parent[ny][nx] = (cy, cx)
                    heapq.heappush(pq, (new_cost, nx, ny))

    return dist, parent

def restore_path(parent, start, end):
    path = []
    y, x = end, start
    while x != -1 and y != -1:
        path.append((y, x))
        y, x = parent[y][x]
    return path[::-1]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist, parent = dijkstra(0, 0, grid, n)

print(dist[n - 1][n - 1])
path = restore_path(parent, n - 1, n - 1)
print(path)
