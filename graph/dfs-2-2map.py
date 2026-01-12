# 2차원 격자에서 상하좌우로 연결된 1의 개수(= 섬/단지 개수)를 구하라
# - 섬의 개수
# - 단지 번호 붙이기 (개수만 구하는 버전)
# - 유기농 배추 (형태만 다름)

# 5
# 1 1 0 0 0
# 1 0 0 1 1
# 0 0 0 1 0
# 1 1 0 0 1
# 0 0 0 1 1

## 4

# input, 방향키, visited
# dfs
# 탐색 (2중for)
# 범위 + visited 조건 확인

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if grid[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny)

count = 0

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1 and not visited[y][x]:
            dfs(x, y)
            count += 1

print(count) # 4
