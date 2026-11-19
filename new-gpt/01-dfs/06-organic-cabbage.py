# 백준 1012번 유기농 배추

# 농부가 배추를 심은 밭이 있어.
# 배추에는 해충이 생길 수 있기 때문에 배추를 보호하는 배추흰지렁이를 놓으려고 해.
# 이 지렁이는 상하좌우로 연결된 배추밭을 이동할 수 있어.
# 따라서 상하좌우로 연결된 배추들은 지렁이 한 마리로 보호할 수 있어.

# 우리가 구해야 할 것은 다음과 같아.
# 각 배추밭에서 필요한 지렁이의 최소 마릿수는 몇 마리일까?
# 즉, 배추가 심어진 칸들이 이루는 연결된 영역의 개수를 구하면 돼.

# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5

# 5
# 1

# import sys
# sys.setrecursionlimit(10**6)

t = int(input())
count = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  checked = [[False] * m for _ in range(n)]
  
  for i in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1

  def dfs(x, y):
    checked[y][x] = True

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx] == 1 and not checked[ny][nx]:
          dfs(nx, ny)

  idx = 0
  for y in range(n):
    for x in range(m):
      if graph[y][x] == 1 and not checked[y][x]:
        idx += 1
        dfs(x, y)

  count.append(idx)

for i in count:
  print(i)
