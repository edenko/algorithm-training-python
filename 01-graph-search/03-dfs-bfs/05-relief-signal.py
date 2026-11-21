# 재난 구조 신호

# N × M 크기의 건물에 여러 개의 구조 신호 발신기가 설치되어 있어.
# 발신기는 매초 상하좌우로 인접한 통로에 신호를 퍼뜨려.
# 건물의 각 칸은 다음 세 가지 상태 중 하나야.
# 값	의미
# 0	신호가 전달될 수 있는 통로
# 1	신호 발신기
# -1	신호가 통과할 수 없는 벽

# 모든 발신기는 0초부터 동시에 신호를 보내기 시작해.
# 신호는 1초에 한 칸씩 퍼지고, 벽을 통과하거나 건물 밖으로 나갈 수 없어.
# 구해야 할 값은 모든 통로가 신호를 받는 데 필요한 최소 시간이야.

# 단, 다음 조건도 고려해야 해.
# - 처음부터 신호가 닿아야 할 통로가 없다면 0을 출력해.
# - 신호를 받을 수 없는 통로가 하나라도 남으면 -1을 출력해.
# - 발신기가 여러 개 있더라도 각각의 신호는 동시에 퍼져.

# 첫째 줄에 N M이 주어져.
# 그다음 N줄에 걸쳐 M개의 정수가 공백으로 주어져.
# - 1 ≤ N, M ≤ 100
# - 발신기는 최소 한 개 이상 존재해.
# - 상하좌우로만 신호가 전달돼.

# 4 6
# 1 0 0 -1 0 0
# 0 0 0 -1 0 1
# 0 -1 0 0 0 0
# 0 0 0 -1 0 0

# 5

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for y in range(n):
  for x in range(m):
    if graph[y][x] == 1:
      q.append((x, y))
      dist[y][x] = 0

while q:
    cx, cy = q.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if dist[ny][nx] == -1 and graph[ny][nx] == 0:
          q.append((nx, ny))
          dist[ny][nx] = dist[cy][cx] + 1

failed = False
for y in range(n):
  for x in range(m):
    if dist[y][x] == -1 and graph[y][x] == 0:
      failed = True

if failed:
  print(-1)
else:
  print(max(map(max, dist)))
