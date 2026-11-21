# 문제 3️⃣ — 바이러스 확산 시뮬레이션

# N × N 격자가 있다.
# 각 칸의 값:
# 0 : 빈 칸
# 1 : 벽
# 2 : 바이러스

# 바이러스는 매 초마다 상하좌우로 동시에 확산된다.
# 벽(1)이 있는 칸으로는 확산되지 않는다.
# S초가 지난 후, 좌표 (x, y)에 있는 값을 출력하라.

from collections import deque

def solution(n, s, cx, cy, grid):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque()
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 2:
                q.append((x, y, 0))

    while q:
        x, y, t = q.popleft()
        if t == s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = 2
                    q.append((nx, ny, t + 1))
        
    return grid[cy][cx]

sol = solution(
    n = 5,
    s = 2,
    cx = 2,
    cy = 2,
    grid = [
        [1,0,2,0,1],
        [0,0,0,0,0],
        [0,1,0,1,0],
        [0,0,0,0,0],
        [1,0,0,0,2],
    ]

)
print(sol) # 2
