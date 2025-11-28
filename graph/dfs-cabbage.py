m, n = map(int, input().split())
grid = [[0] * m for _ in range(n)]
checked = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    x, y = map(int, input().split())
    grid[y][x] = 1

def dfs(x, y):
    checked[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] and not checked[ny][nx]:
                dfs(nx, ny)

count = 0

for y in range(n):
    for x in range(m):
        if grid[y][x] and not checked[y][x]:
            count += 1
            dfs(x, y)

print(count)
