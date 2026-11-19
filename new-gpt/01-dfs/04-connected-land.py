# 연결된 땅 덩어리 개수 구하기
# 다음 지도에서 상하좌우로 연결된 1의 영역이 몇 개인지 출력하는 프로그램을 만들어보자.

# 재귀 DFS 사용하기
# dfs(r, c) 형태로 함수 만들기
# 상하좌우만 탐색하기
# 방문 배열을 이용해서 중복 방문 방지하기
# 범위를 벗어난 좌표는 탐색하지 않기
# 이미 방문했거나 바다인 칸은 탐색하지 않기
# 전체 지도를 돌면서 연결된 영역의 개수를 세기

# 2

graph = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

n, m = len(graph), len(graph[0])
checked = [[False] * m for _ in range(n)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  checked[y][x] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < m and 0 <= ny < n:
      if graph[ny][nx] == 1 and not checked[ny][nx]:
        dfs(nx, ny)

for y in range(n):
  for x in range(m):
    if graph[y][x] == 1 and not checked[y][x]:
      count += 1
      dfs(x, y)

print(count)
