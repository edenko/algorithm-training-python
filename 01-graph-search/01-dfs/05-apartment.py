# 백준 2667번 단지번호붙이기

# 정사각형 지도에 집들이 표시되어 있어.
# - 1은 집이 있는 칸
# - 0은 집이 없는 칸
# - 상하좌우로 연결된 집들은 같은 단지
# - 대각선으로만 붙어 있는 집들은 다른 단지

# ① 총 몇 개의 단지가 있는가?
# ② 각 단지에 집이 몇 개씩 있는가?

# 단지별 집의 개수는 오름차순으로 출력해야 해.

# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3 7 8 9

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
checked = [[False] * n for _ in range(n)]
count = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  checked[y][x] = True
  size = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n:
      if graph[ny][nx] == 1 and not checked[ny][nx]:
        size += dfs(nx, ny)

  return size

size = 0
for y in range(n):
  for x in range(n):
    if graph[y][x] == 1 and not checked[y][x]:
      count.append(dfs(x, y))

print(len(count), *sorted(count), sep='\n')
