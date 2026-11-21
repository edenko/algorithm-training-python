# 백준 7576번 토마토

# 토마토가 가로 M칸, 세로 N칸의 상자에 들어 있어.

# 각 칸은 세 가지 상태 중 하나야.
# 값	의미
# 1	익은 토마토
# 0	익지 않은 토마토
# -1	토마토가 없는 칸

# 하루가 지나면 익은 토마토와 상하좌우로 인접한 익지 않은 토마토가 익게 돼.
# 모든 토마토가 익는 데 필요한 최소 일수를 출력해야 해.
# 처음부터 모든 토마토가 익어 있다면 0, 아무리 시간이 지나도 전부 익힐 수 없다면 -1을 출력해야 해.

# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 8

# 1 -1 0
# 0 -1 0
# 0 -1 0

# -1

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[-1] * m for _ in range(n)]
q = deque()

for y in range(n):
  for x in range(m):
    if graph[y][x] == 1:
      q.append((x, y))
      dist[y][x] = 0

while q:
  x, y = q.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < m and 0 <= ny < n:
      if dist[ny][nx] == -1 and graph[ny][nx] == 0:
        dist[ny][nx] = dist[y][x] + 1
        q.append((nx, ny))

failed = False
for y in range(n):
  for x in range(m):
    if dist[y][x] == -1 and graph[y][x] == 0:
      failed = True

if failed:
    print(-1)
else:
  print(max(map(max, dist)))
