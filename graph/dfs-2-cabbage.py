# 유기농 배추 (BOJ 1012)
# 유기농 배추밭에서 배추가 심어져 있는 위치(1) 들이 주어진다.
# 배추흰지렁이는 상·하·좌·우로 연결된 배추 덩어리마다 1마리가 필요하다.

# 👉 필요한 지렁이 수 = 배추 덩어리(연결 요소) 개수

# 5 5
# 1 1
# 1 2
# 2 2
# 3 4
# 4 4

## 2

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
