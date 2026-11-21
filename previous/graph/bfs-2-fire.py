# BOJ 4179 — 불(Fire)
# 두 개의 BFS를 분리해서 실행
# 불이 먼저 퍼지고 그 다음에 사람이 이동해야 함 -> dist가 두개
# 불은 퍼질 때의 시간을 기록. 숫자가 낮을수록 먼저 닿은거임.

# 4 4
# ####
# #JF#
# #..#
# #..#

## 3

from collections import deque

m, n = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distFire = [[-1] * m for _ in range(n)]
distJ = [[-1] * m for _ in range(n)]

qFire = deque()
qJ = deque()

for y in range(n):
    for x in range(m):
        if grid[y][x] == 'F':
            distFire[y][x] = 0
            qFire.append((x, y))
        elif grid[y][x] == 'J':
            distJ[y][x] = 0
            qJ.append((x, y))

while qFire:
    x, y = qFire.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] != '#' and distFire[ny][nx] == -1:
                distFire[ny][nx] = distFire[y][x] + 1
                qFire.append((nx, ny))

while qJ:
    x, y = qJ.popleft()

    if x == 0 or x == m - 1 or y == 0 or y == n -1:
        print(distJ[y][x] + 1)
        exit()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if grid[ny][nx] == '.' and distJ[ny][nx] == -1:
                if distFire[ny][nx] != -1 and distFire[ny][nx] <= distJ[y][x] + 1: ## 이게 핵심 !
                    continue
                    
                distJ[ny][nx] = distJ[y][x] + 1
                qJ.append((nx, ny))

print('IMPOSSIBLE')
