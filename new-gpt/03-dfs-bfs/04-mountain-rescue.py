# 산악 구조대의 최단 이동

# 산악 구조대가 N × M 크기의 지형에서 조난자를 구출하려고 해.
# 각 칸에는 해당 위치의 높이가 적혀 있어.
# 구조대는 왼쪽 위 (0, 0)에서 출발해 오른쪽 아래 (M-1, N-1)에 도착해야 해.

# 다음 규칙에 따라 이동할 수 있어.
# - 상하좌우로 인접한 칸에만 이동할 수 있어.
# - 현재 칸과 다음 칸의 높이 차이가 K 이하여야 해.
# - 한 번 이동할 때마다 정확히 1분이 걸려.
# - 출발점에서 도착점까지 걸리는 최소 시간을 구해야 해.
# - 도착할 수 없다면 -1을 출력해야 해.

# 첫째 줄에 N M K가 주어져.
# 이후 N줄에 걸쳐 각 칸의 높이가 주어져.
# - 1 ≤ N, M ≤ 100
# - 0 ≤ K ≤ 100
# - 각 칸의 높이는 1 이상 100 이하

# 4 5 2
# 1 2 8 9 10
# 2 3 7 12 11
# 10 3 4 13 20
# 11 12 5 14 21

# -1

# 3 4 2
# 1 2 8 9
# 2 3 5 10
# 3 4 6 8

# 5

from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
  q = deque([(x, y)])
  dist[y][x] = 0

  while q:
    cx, cy = q.popleft()

    # if (cx, cy) == (n - 1, m - 1):
    if cx == m - 1 and cy == n - 1:
      return

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if abs(graph[cy][cx] - graph[ny][nx]) <= k and dist[ny][nx] == -1:
          q.append((nx, ny))
          dist[ny][nx] = dist[cy][cx] + 1

bfs(0, 0, k)

if dist[n - 1][m - 1] == -1:
  print(-1)
else:
  print(dist[n - 1][m - 1])
