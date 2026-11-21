# 백준 2178번 미로 탐색

# N행 M열로 이루어진 미로가 있어.
# - 1은 이동할 수 있는 칸
# - 0은 이동할 수 없는 칸(벽)
# - 시작 위치는 왼쪽 위 (0, 0)
# - 도착 위치는 오른쪽 아래 (N-1, M-1)
# - 상하좌우로만 이동할 수 있고 대각선 이동은 불가능해.

# 목표는 시작 위치부터 도착 위치까지 이동하면서 지나야 하는 최소 칸 수를 구하는 거야.
# 중요한 점은 시작 칸과 도착 칸도 개수에 포함한다는 거야.
# 예를 들어 시작 칸에서 오른쪽으로 한 칸 이동했다면 이동 횟수는 1번이지만, 지나온 칸 수는 2개야.

# 4 6
# 101111
# 101010
# 101011
# 111011

# 15

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque([(x, y)])
  dist = [[-1] * m for _ in range(n)]
  dist[y][x] = 1

  while q:
    cx, cy = q.popleft()

    if cx == m - 1 and cy == n - 1:
      return dist[cy][cx]

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if dist[ny][nx] == -1 and graph[ny][nx] == 1:
          dist[ny][nx] = dist[cy][cx] + 1
          q.append((nx, ny))

print(bfs(0, 0))
