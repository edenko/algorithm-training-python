# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

# 그림 (BOJ 1926)
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

checked = [[False] * m for _ in range(n)]

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
            if grid[ny][nx] == 1 and not checked[ny][nx]:
                dfs(nx, ny)

result = []

for y in range(n):
    for x in range(m):
        if grid[y][x] == 1 and not checked[y][x]:
            area = 0
            dfs(x, y)
            result.append(area)

print(len(result)) # 4
print(max(result)) # 9
