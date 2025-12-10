# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7

# 고도 표시 - 고도가 높으면 비가 와도 안 잠기는 거, 2만큼 비가 오면 고도가 2인 곳까지 잠김
# "높이" 조건에 따라 여러 번 DFS 실행
import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
    global checked
    checked[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if grid[ny][nx] > h and not checked[ny][nx]:
                dfs(nx, ny, h)

maxHeight = max(map(max, grid))
result = []

for i in range(maxHeight + 1):
    checked = [[False] * n for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if grid[y][x] > i and not checked[y][x]:
                dfs(x, y, i)
                cnt += 1
    result.append(cnt)

print(max(result)) # 5
