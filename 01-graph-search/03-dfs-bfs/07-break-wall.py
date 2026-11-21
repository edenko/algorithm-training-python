# 백준 2206번 벽 부수고 이동하기

# N × M 크기의 미로가 있어.
# 각 칸은 다음 두 종류 중 하나야.
# 값	의미
# 0	이동할 수 있는 빈 칸
# 1	이동할 수 없는 벽

# 너는 왼쪽 위 (0, 0)에서 시작해서 오른쪽 아래 (M-1, N-1)까지 이동해야 해.

# 이동 규칙은 다음과 같아.
# - 상하좌우로 한 칸씩 이동할 수 있어.
# - 일반적으로 벽(1)은 지나갈 수 없어.
# - 단, 이동하는 도중 벽을 최대 한 개까지 부술 수 있어.
# - 벽을 부수면 그 벽이 있던 칸으로 이동할 수 있어.
# - 시작 칸과 도착 칸도 포함해 지나온 칸의 개수가 가장 적은 경로를 구해야 해.
# - 도착할 수 없다면 -1을 출력해.
# 중요: 벽을 반드시 부숴야 하는 건 아니야. 부수지 않고 도착할 수 있다면 그렇게 이동해도 돼.

# 첫째 줄에 N M이 주어져.
# 이후 N줄에 걸쳐 길이가 M인 0과 1로 이루어진 문자열이 주어져.
# - 1 ≤ N, M ≤ 1,000
# - N × M ≤ 1,000,000
# - 시작점 (0, 0)과 도착점 (M-1, N-1)은 항상 빈 칸이야.

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 15

# 4 4
# 0111
# 1111
# 1111
# 1110

# -1

# 3 3
# 000
# 000
# 000

# 5

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(cx, cy):
  q = deque([(cx, cy, 0)])
  dist[cy][cx][0] = 1

  while q:
    x, y, b = q.popleft()

    if x == m - 1 and y == n - 1:
      return dist[y][x][b]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 0 and dist[ny][nx][b] == 0:
          q.append((nx, ny, b))
          dist[ny][nx][b] = dist[y][x][b] + 1
        elif graph[ny][nx] == 1 and dist[ny][nx][1] == 0 and b == 0:
          q.append((nx, ny, 1))
          dist[ny][nx][1] = dist[y][x][b] + 1

  return -1

print(bfs(0, 0))
