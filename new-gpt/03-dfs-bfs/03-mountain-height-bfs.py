# 높이 차이가 있는 산악 지대

# N × M 크기의 산악 지대가 있어. 각 칸에는 해당 지형의 높이가 적혀 있어.
# 탐험가는 현재 위치에서 상하좌우로 인접한 칸으로 이동할 수 있어.
# 하지만 다음 조건을 만족해야 해.

# 현재 칸과 다음 칸의 높이 차이가 K 이하일 때만 이동할 수 있어.
# 예를 들어 K = 2일 때:
# - 높이 3 → 높이 5: 이동 가능
# - 높이 7 → 높이 6: 이동 가능
# - 높이 2 → 높이 6: 이동 불가능
# 이 조건으로 서로 이동할 수 있는 칸들을 하나의 탐험 가능 구역으로 정의할게.

# 구해야 하는 값은 두 가지야.
# 1. 탐험 가능 구역의 총개수
# 2. 가장 큰 탐험 가능 구역에 포함된 칸의 개수

# 첫째 줄에 N M K가 공백으로 주어져.
# 이후 N줄에 걸쳐 M개의 지형 높이가 공백으로 주어져.
# - 1 ≤ N, M ≤ 100
# - 0 ≤ K ≤ 100
# - 각 지형의 높이는 1 이상 100 이하

# 4 5 2
# 1 2 8 9 10
# 2 3 7 12 11
# 10 3 4 13 20
# 11 12 5 14 21

# 4
# 8

from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
checked = [[False] * m for _ in range(n)]
answer = 0
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, k):
  q = deque([(x, y)])
  checked[y][x] = True
  size = 1

  while q:
    cx, cy = q.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        # if graph[cy][cx] - k <= graph[ny][nx] <= graph[cy][cx] + k and not checked[ny][nx]:
        if abs(graph[cy][cx] - graph[ny][nx]) <= k and not checked[ny][nx]:
          checked[ny][nx] = True
          size += 1
          q.append((nx, ny))

  return size

for y in range(n):
  for x in range(m):
    if not checked[y][x]:
      count += 1
      answer = max(answer, bfs(x, y, k))

print(count)
print(answer)
