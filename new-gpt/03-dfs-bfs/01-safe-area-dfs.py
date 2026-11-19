# 백준 2468 안전 영역

# N × N 크기의 지역이 있어. 각 칸에는 해당 지역의 높이가 적혀 있어.
# 비가 h만큼 내리면 높이가 h 이하인 지역은 물에 잠겨.
# 반대로 높이가 h보다 높은 지역은 잠기지 않아.
# 물에 잠기지 않은 칸들이 상하좌우로 연결되어 있으면 하나의 안전 영역으로 봐.
# 문제에서 구해야 하는 것은 다음과 같아.
# 비의 높이를 여러 가지로 바꿔보았을 때, 안전 영역의 개수가 가장 많아지는 경우의 개수.
# 여기서 중요한 건 비가 전혀 내리지 않는 경우도 포함한다는 점이야.

# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# 5

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
height = max(map(max, graph))
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for h in range(height + 1):
  checked = [[False] * n for _ in range(n)]
  cnt = 0

  def dfs(x, y):
    checked[y][x] = True

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] > h and not checked[ny][nx]:
          dfs(nx, ny)

  for y in range(n):
    for x in range(n):
      if graph[y][x] > h and not checked[y][x]:
        cnt += 1
        dfs(x, y)

  answer = max(answer, cnt)

print(answer)
