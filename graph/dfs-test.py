import sys
sys.setrecursionlimit(10**6)

t = int(input())
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    checked[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] == 1 and not checked[ny][nx]:
                dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    checked = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1

    cnt = 0

    for y in range(n):
        for x in range(m):

            if grid[y][x] == 1 and not checked[y][x]:
                dfs(x, y)
                cnt += 1

    result.append(cnt)

print(result)
