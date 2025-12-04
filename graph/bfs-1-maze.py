# 4 4
# 1011
# 1111
# 0011
# 1111

# BFS Level 1 — 미로 탐색 (BOJ 2178)
# BFS는 “현재 위치에서 갈 수 있는 모든 다음 위치를 한 번에 탐색 → 그 다음 레벨로 이동”
# 즉, 최단 거리 보장
# DFS로는 최단거리가 안 된다 → 백트래킹 + 전역 최소 갱신이 필요해서 비효율적

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

checked = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    checked[0][0] = True
    
    dist[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if grid[ny][nx] == 1 and not checked[ny][nx]:
                    checked[ny][nx] = True

                    dist[ny][nx] = dist[y][x] + 1

                    q.append((nx, ny))
    
bfs()

print(dist[n - 1][m - 1]) # 7
