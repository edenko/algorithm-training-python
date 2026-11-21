# 백준 7562번 — 나이트의 이동

# 체스판 위에 나이트가 있어.
# 나이트는 현재 위치에서 정해진 8가지 방향으로만 이동할 수 있어.
# 현재 위치에서 목표 위치까지 이동하는 최소 횟수를 구하는 문제야.

# 중요한 조건은 다음과 같아.
# - 체스판은 l × l 크기의 정사각형이야.
# - 좌표는 0부터 l-1까지 사용할 수 있어.
# - 나이트는 한 번 이동할 때마다 1회로 계산해.
# - 체스판 밖으로는 이동할 수 없어.
# - 테스트 케이스가 여러 개 주어져.

# 첫째 줄에는 테스트 케이스의 개수 T가 주어져.
# 각 테스트 케이스는 다음 세 줄로 이루어져.
# 1. 체스판 한 변의 길이 l
# 2. 시작 좌표 x y
# 3. 도착 좌표 x y

# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1

# 5
# 28
# 0

from collections import deque

t = int(input())
answer = []

dx = [2, 1, 2, 1, -1, -2, -1, -2]
dy = [1, 2, -1, -2, 2, 1, -2, -1]

for _ in range(t):
  n = int(input())
  sx, sy = map(int, input().split())
  ex, ey = map(int, input().split())

  def bfs(x, y):
    dist = [[-1] * n for _ in range(n)]
    dist[y][x] = 0
    q = deque([(x, y)])
  
    while q:
      cx, cy = q.popleft()
  
      if ex == cx and ey == cy:
        return dist[cy][cx]

      for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
          if dist[ny][nx] == -1:
            dist[ny][nx] = dist[cy][cx] + 1
            q.append((nx, ny))

  answer.append(bfs(sx, sy))

for el in answer:
  print(el)
