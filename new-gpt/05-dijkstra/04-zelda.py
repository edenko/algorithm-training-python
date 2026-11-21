# 백준 4485번 — 녹색 옷 입은 애가 젤다지?

# N × N 크기의 동굴이 있어.
# 각 칸에는 숫자가 적혀 있고, 그 칸으로 이동하면 해당 숫자만큼의 루피를 잃어버려.
# 우리는 동굴의 왼쪽 위 (0, 0)에서 출발해서 오른쪽 아래 (N-1, N-1)까지 이동해야 해.
# 목표는 잃어버리는 루피의 총합을 최소화하는 것이야.
# 이동은 상하좌우 네 방향으로만 할 수 있어.
# 시작 칸 (0, 0)의 비용도 포함해야 해.

# 이 문제는 여러 테스트 케이스가 주어지는 문제야.
# N이 입력되고, 다음에 N × N 동굴 정보가 나와.
# 이 과정이 반복되며 N = 0이 입력되면 종료해야 해.

# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 0

# Problem 1: 20
# Problem 2: 19
# Problem 3: 36

import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
idx = 0

while True:
  n = int(input())

  if n == 0:
    break

  idx += 1
  graph = [list(map(int, input().split())) for _ in range(n)]
  INF = float('inf')
  dist = [[INF] * n for _ in range(n)]
  dist[0][0] = graph[0][0]

  heap = []
  heapq.heappush(heap, (graph[0][0], 0, 0))

  while heap:
    cost, cx, cy = heapq.heappop(heap)

    if cost > dist[cy][cx]:
      continue

    for i in range(4):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        new_cost = cost + graph[ny][nx]
        if new_cost < dist[ny][nx]:
          dist[ny][nx] = new_cost
          heapq.heappush(heap, (new_cost, nx, ny))

  print('Problem ' + str(idx) + ': ' + str(dist[n - 1][n - 1])) # Problem 1: 20
