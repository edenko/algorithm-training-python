# 섬의 개수 (BOJ 4963)

# 지도에서 1은 땅, 0은 바다를 의미한다.
# 땅은 상·하·좌·우 + 대각선(8방향) 으로 연결될 수 있다.

# 👉 연결된 땅 덩어리(섬)의 개수를 구하라.

# 6 5
# 1 0 1 0 1 0
# 0 1 0 1 0 1
# 1 0 0 0 1 0
# 0 1 0 0 0 1
# 1 0 1 0 1 0

## 1

w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

checked = [[False] * w for _ in range(h)]

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    checked[y][x] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < w and 0 <= ny < h:
            if grid[ny][nx] == 1 and not checked[ny][nx]:
                dfs(nx, ny)

count = 0

for y in range(h):
    for x in range(w):
        if grid[y][x] == 1 and not checked[y][x]:
            count += 1
            dfs(x, y)

print(count)
