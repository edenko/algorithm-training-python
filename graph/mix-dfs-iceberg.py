# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0

# 빙산 (BOJ 2573)

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    melt_arr = [[0] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if grid[y][x] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[ny][nx] == 0:
                            cnt += 1
                melt_arr[y][x] = cnt
    return melt_arr

def dfs(x, y, checked):
    checked[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] > 0 and not checked[ny][nx]:
                dfs(nx, ny, checked)

def count_ice():
    count = 0
    checked = [[False] * m for _ in range(n)]

    for y in range(n):
        for x in range(m):
            if grid[y][x] > 0 and not checked[y][x]:
                dfs(x, y, checked)
                count += 1
    return count

year = 0

while True:
    melt_arr = melt()
    year += 1

    for y in range(n):
        for x in range(m):
            grid[y][x] = max(0, grid[y][x] - melt_arr[y][x])

    ice = count_ice()
    if ice > 1:
        print(year)
        break
    elif ice == 0:
        print(0)
        break
