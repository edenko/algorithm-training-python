# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

# 연구소 (BOJ 14502)
# 0 = 빈 칸 / 1 = 벽 / 2 = 바이러스
# Step 1. 모든 빈칸 위치 저장
# Step 2. 빈칸 중 3개를 뽑는 모든 조합 생성 (순서 없는 조합 = combinations)
# Step 3. 그 조합별로: 벽 3개를 세움, BFS로 바이러스 퍼트린 후 안전지대 계산, 최댓값 갱신, copy 사용

from itertools import combinations
import copy
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
virus = []

for y in range(n):
    for x in range(m):
        if grid[y][x] == 0:
            empty.append((x, y))
        elif grid[y][x] == 2:
            virus.append((x, y))

def bfs(temp):
    q = deque()
    for x, y in virus:
        q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append((nx, ny))

    cnt = 0
    for y in range(n):
        for x in range(m):
            if temp[y][x] == 0:
                cnt += 1
    return cnt 

answer = 0

for walls in combinations(empty, 3):
    temp = copy.deepcopy(grid)

    for x, y in walls:
        temp[y][x] = 1
    
    safe = bfs(temp)
    answer = max(answer, safe)

print(answer) # 27
