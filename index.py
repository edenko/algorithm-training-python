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
