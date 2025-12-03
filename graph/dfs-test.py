n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
count = 0

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        
        if grid[i][j] == 1 and not visited[i][j]:
            count += 1
            dfs(i, j)


print(count)
