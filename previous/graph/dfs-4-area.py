# 영역 구하기 (BOJ 2583)

# N × M 크기의 종이가 있고,
# 그 위에 K개의 직사각형 영역이 색칠되어 있다.

# 색칠된 영역: 막힌 영역

# 색칠되지 않은 영역: 빈 영역

# 👉 서로 상·하·좌·우로 연결된 빈 영역의 개수와
# 👉 각 영역의 넓이를 구하라.

# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

## 3
## 1 7 13

import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
checked = [[False] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    checked[y][x] = True
    global area
    area += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] == 0 and not checked[ny][nx]:
                dfs(nx, ny)

result = []

for y in range(n):
    for x in range(m):

        if grid[y][x] == 0 and not checked[y][x]:
            area = 0
            dfs(x, y)
            result.append(area)

print(len(result)) # 3
print(*sorted(result)) # 1 7 13
