# 2D Grid 최소 비용 찾기 (2D 다익스트라)

# 문제 설명
# N×N 맵이 있고, 각 칸에는 지나가는 데 필요한 비용이 적혀 있다.
# 왼쪽 위 (0,0)에서
# 오른쪽 아래 (N-1, N-1)까지 이동하는 데 필요한 최소 비용을 구하라.
# 이동 가능 방향: 상하좌우

# 3
# 5 5 4
# 3 9 1
# 3 2 7

# 20

import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(x, y, grid, n):
    dist = [[INF] * n for _ in range(n)]
    dist[y][x] = grid[y][x]
    pq = []
    heapq.heappush(pq, (grid[y][x], y, x))

    while pq:
        cost, cy, cx = heapq.heappop(pq)

        if cost > dist[cy][cx]:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + grid[ny][nx]
                if new_cost < dist[ny][nx]:
                    dist[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost, ny, nx))
                    
    return dist

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist = dijkstra(0, 0, grid, n)

print(dist[n - 1][n - 1])
