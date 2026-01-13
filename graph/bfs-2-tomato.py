# 토마토 (BOJ 7576)
# BFS를 **여러 개의 시작점(1)**에서 동시에 시작
# queue에 모든 익은 토마토를 처음부터 넣음
# 전부 익지 못하면 -1

# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

## 8

from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
checked = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

q = deque()

for y in range(n):
    for x in range(m):
        if grid[y][x] == 1:
            checked[y][x] = True
            q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if grid[ny][nx] == 0 and not checked[ny][nx]:
                    grid[ny][nx] = grid[y][x] + 1
                    checked[ny][nx] = True
                    q.append((nx, ny))

    for y in range(n):
        for x in range(m):
            if grid[y][x] == 0:
                return -1
    
    return max(map(max, grid)) - 1
    
print(bfs())
