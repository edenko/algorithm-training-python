# 필수 경유지 미로

# N × M 크기의 건물 내부에 미로가 있어.

# 각 칸은 다음 네 가지 중 하나야.
# 문자	의미
# S	출발점
# E	도착점
# C	반드시 방문해야 하는 체크포인트
# .	이동할 수 있는 빈 공간
# #	이동할 수 없는 벽

# 탐험가는 상하좌우로만 이동할 수 있고, 한 칸 이동할 때마다 1초가 걸려.
# 출발점 S에서 출발하여 체크포인트 C를 반드시 한 번 이상 방문한 뒤 도착점 E로 이동하는 최소 시간을 구해야 해.
# 도착할 수 없다면 -1을 출력해야 해.
# 이번 문제에는 S, C, E가 각각 정확히 하나씩 존재해.

# 첫째 줄에 N M이 주어져.
# 이후 N줄에 걸쳐 길이가 M인 문자열이 공백 없이 주어져.
# - 1 ≤ N, M ≤ 100
# - 이동 가능 방향은 상하좌우
# - 모든 이동 비용은 1초
# - S, C, E는 각각 한 개씩 존재

# 5 7
# S..#... 
# ##.#.#.
# ...C...
# .#.###.
# ...#..E

# 10

# 3 3
# S#C
# ###
# E..

# -1

from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(n)]
sx, sy, cx, cy, ex, ey = 0, 0, 0, 0, 0, 0
failed = False

for y in range(n):
  for x in range(m):
    if graph[y][x] == 'S':
      sx, sy = x, y
    elif graph[y][x] == 'C':
      cx, cy = x, y
    elif graph[y][x] == 'E':
      ex, ey = x, y

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(rx, ry, ax, ay):
  dist = [[-1] * m for _ in range(n)]
  dist[ry][rx] = 0
  q = deque([(rx, ry)])

  while q:
    x, y = q.popleft()

    if x == ax and y == ay:
      return dist[y][x]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if dist[ny][nx] == -1 and graph[ny][nx] != '#':
          q.append((nx, ny))
          dist[ny][nx] = dist[y][x] + 1

  return -1

second = bfs(cx, cy, ex, ey)
first = bfs(sx, sy, cx, cy)

print(-1 if first == -1 or second == -1 else first + second)
