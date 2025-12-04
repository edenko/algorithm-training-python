# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 1. input, visited, 좌표 
# 2. dfs
# 3. 탐색
# 4. 범위 및 조건 정리

# 총 단지 수 구하기
# 각 단지에 속한 집의 수 구하기
# 집의 수를 오름차순으로 출력하기

n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global house
    house += 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

result = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            house = 0
            dfs(i, j)
            result.append(house)


print(len(result))
for node in sorted(result):
    print(node)
