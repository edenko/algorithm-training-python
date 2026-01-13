# 게임 맵 최단거리 (Programmers)

# 캐릭터는 (0, 0)에서 출발해서
# (n-1, m-1)까지 이동해야 한다.

# 1 : 이동 가능
# 0 : 벽 (이동 불가)
# 이동 방향: 상·하·좌·우
# 목표: 최단 거리

# 👉 도착할 수 없으면 -1 반환

# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
## 11

from collections import deque
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    checked = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0, 0))
    checked[0][0] = True
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        
        if x == m - 1 and y == n - 1:
            return dist[y][x]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] == 1 and not checked[ny][nx]:
                    checked[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((nx, ny))

    if dist[n - 1][m - 1] < 1:
        return -1
    