# 백준 14923번 · 미로 탈출

# N × M 크기의 미로가 있어.
# 숫자	의미
# 0	이동 가능한 빈 칸
# 1	이동할 수 없는 벽

# 주인공은 주어진 시작 위치에서 출발해 목표 위치까지 이동해야 해.
# 이동 규칙은 다음과 같아.
# - 상하좌우로 한 칸씩 이동할 수 있어.
# - 벽은 통과할 수 없어.
# - 단, 마법을 사용해서 벽을 최대 한 개까지 부술 수 있어.
# - 벽을 부수면 그 칸으로 이동할 수 있어.
# - 벽을 반드시 부술 필요는 없어.
# - 목표 위치까지 이동하는 최소 이동 횟수를 구해야 해.
# - 도착할 수 없다면 -1을 출력해.

# N, M: 미로의 행과 열 개수
# Hx Hy: 시작 위치
# Ex Ey: 목표 위치
# 이후 N줄: 각 행에 M개의 숫자가 공백으로 구분되어 주어져.
# 좌표는 1부터 시작하고, 첫 번째 값이 행, 두 번째 값이 열이야.
# 1 ≤ N, M ≤ 1,000

# 3 3
# 1 1
# 3 3
# 0 1 0
# 1 1 0
# 0 0 0

# 4

# 2 3
# 1 3
# 2 3
# 0 0 0
# 0 0 0

# 1

from collections import deque

n, m = map(int, input().split())
hy, hx = map(int, input().split())
ey, ex = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(hx, hy, ex, ey):
  q = deque([(hx, hy, 0)])
  dist[hy][hx][0] = 0

  while q:
    x, y, b = q.popleft()

    if x == ex and y == ey:
      return dist[y][x][b]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 0 and dist[ny][nx][b] == -1:
          q.append((nx, ny, b))
          dist[ny][nx][b] = dist[y][x][b] + 1
        elif graph[ny][nx] == 1 and dist[ny][nx][1] == -1 and b == 0:
          q.append((nx, ny, 1))
          dist[ny][nx][1] = dist[y][x][b] + 1

  return -1

print(bfs(hx - 1, hy - 1, ex - 1, ey - 1))
