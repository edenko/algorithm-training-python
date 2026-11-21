# 백준 1600번 — 말이 되고픈 원숭이

# 원숭이가 H × W 크기의 격자 왼쪽 위에서 출발해 오른쪽 아래까지 이동해야 해.
# 원숭이에게는 두 가지 이동 방법이 있어.

# 4방향
# 일반 이동
# 위, 아래, 왼쪽, 오른쪽으로 한 칸 이동할 수 있어.
# 몇 번이든 사용할 수 있어.

# 8방향
# 말 이동 (체스 나이트)
# 가로로 2칸 + 세로로 1칸, 또는 가로로 1칸 + 세로로 2칸 점프할 수 있어.
# 단, 최대 K번만 사용할 수 있어.

# 일반 이동과 말 이동 모두 한 번 움직이면 이동 횟수가 1 증가해.
# 목표는 출발점 (0, 0)에서 도착점 (H-1, W-1)까지의 최소 이동 횟수를 구하는 거야.
# 도착할 수 없다면 -1을 출력해야 해.
# 격자에서 0은 이동 가능한 칸, 1은 장애물이야. 말 이동도 장애물인 칸에 착지할 수 없어. 
# 다만 점프하는 도중 지나치는 칸은 장애물이어도 괜찮아.

# K
# W H
# 격자 H줄

# 1
# 4 4
# 0 0 0 0
# 1 0 0 0
# 0 0 1 0
# 0 1 0 0

# 4

# 2
# 5 2
# 0 0 1 1 0
# 0 0 1 1 0

# -1

from collections import deque

k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
dist[0][0][0] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mx = [2, 2, 1, 1, -2, -2, -1, -1]
my = [1, -1, 2, -2, -1, 1, -2, 2]

def bfs():
  q = deque([(0, 0, 0)])

  while q:
    x, y, used = q.popleft()

    if x == m - 1 and y == n - 1:
      return dist[y][x][used]

    if used < k:
      for i in range(8):
        nx = x + mx[i]
        ny = y + my[i]

        if 0 <= nx < m and 0 <= ny < n:
          if graph[ny][nx] == 0 and dist[ny][nx][used + 1] == -1:
            dist[ny][nx][used + 1] = dist[y][x][used] + 1
            q.append((nx, ny, used + 1))

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 0 and dist[ny][nx][used] == -1:
          dist[ny][nx][used] = dist[y][x][used] + 1
          q.append((nx, ny, used))

  return -1

print(bfs())