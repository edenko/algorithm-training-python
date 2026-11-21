# 전력 공급 구역

# 어느 도시에는 N × M 크기의 전력망이 있어.
# 각 칸의 값은 다음을 의미해.
# - 1: 전기가 흐를 수 있는 전력 설비
# - 0: 전기가 흐를 수 없는 지역
# 전력은 상하좌우로 인접한 설비 사이에서만 이동할 수 있어. 대각선으로는 이동할 수 없어.
# 연결된 설비들은 하나의 전력 공급 구역을 이루어.

# 이 도시에서 구해야 할 값은 다음 두 가지야.
# 1. 전력 공급 구역이 총 몇 개인가?
# 2. 가장 큰 전력 공급 구역에는 설비가 몇 개 있는가?

# 5 6
# 1 1 0 0 1 1
# 1 0 0 0 1 0
# 0 0 1 1 0 0
# 0 0 1 0 0 1
# 1 1 0 0 1 1

# 5

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
checked = [[False] * m for _ in range(n)]
answer = 0
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque([(x, y)])
  checked[y][x] = True
  size = 1

  while q:
    cx, cy = q.popleft()

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 1 and not checked[ny][nx]:
          checked[ny][nx] = True
          size += 1
          q.append((nx, ny))

  return size

for y in range(n):
  for x in range(m):
    if graph[y][x] == 1 and not checked[y][x]:
      count += 1
      answer = max(answer, bfs(x, y))

print(count)
print(answer)
