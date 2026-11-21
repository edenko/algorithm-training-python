# 백준 1194번 달이 차오른다, 가자

# 민식이는 미로에 갇혀 있어.
# 미로에는 다음과 같은 칸들이 등장해.

# 문자	의미
# 0	민식이의 시작 위치
# 1	미로의 출구
# .	이동할 수 있는 빈칸
# #	지나갈 수 없는 벽
# a ~ f	열쇠
# A ~ F	잠긴 문

# 예를 들어 A 문을 지나가려면 반드시 a 열쇠가 있어야 해.
# B 문을 지나가려면 b 열쇠가 필요하지.
# 열쇠를 한 번 획득하면 계속 가지고 있고, 문을 지나가도 열쇠가 사라지지 않아.
# 목표는 시작점 0에서 출구 1까지 최소 몇 번 이동해야 하는지 구하는 것이야. 
# 이동할 수 없다면 -1을 출력해.
# 이동은 상하좌우 4방향이고, 한 칸 이동할 때마다 비용은 1이야.

# 1 7
# 0.a.A.1

# 6

# 2 3
# 0A1
# a##

# 4

# 2 3
# 0A1
# ###

# -1

from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]
dist = [[[-1] * 64 for _ in range(m)] for _ in range(n)]
sx, sy, ex, ey = 0, 0, 0, 0

for y in range(n):
  for x in range(m):
    if graph[y][x] == '0':
      sx, sy = x, y
    elif graph[y][x] == '1':
      ex, ey = x, y

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

al = ['a', 'b', 'c', 'd', 'e', 'f']
ala = ['A', 'B', 'C', 'D', 'E', 'F']

def bfs(sx, sy, ex, ey):
  mask = 0
  q = deque([(sx, sy, mask)])
  dist[sy][sx][mask] = 0

  while q:
    x, y, mask = q.popleft()

    if x == ex and y == ey:
      return dist[y][x][mask]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] != '#':
          if graph[ny][nx] in al:
            bit = ord(graph[ny][nx]) - ord('a')
            new_mask = mask | (1 << bit)
            if dist[ny][nx][new_mask] == -1:
              dist[ny][nx][new_mask] = dist[y][x][mask] + 1
              q.append((nx, ny, new_mask))

          elif graph[ny][nx] in ala:
            bit = ord(graph[ny][nx]) - ord('A')
            if mask & (1 << bit) and dist[ny][nx][mask] == -1:
              dist[ny][nx][mask] = dist[y][x][mask] + 1
              q.append((nx, ny, mask))

          else:
            if dist[ny][nx][mask] == -1:
              dist[ny][nx][mask] = dist[y][x][mask] + 1
              q.append((nx, ny, mask))

  return -1

print(bfs(sx, sy, ex, ey))
