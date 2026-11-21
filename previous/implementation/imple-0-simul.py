# 문제 2️⃣ — 동시 이동 시뮬레이션

# N × N 격자가 있다.
# 각 칸에는 0(빈칸) 또는 1(물체) 가 있다.
# 한 턴에 모든 물체는 동시에 아래로 이동한다.
# 아래 칸이 격자 밖이거나 이미 물체가 있으면 이동하지 않는다.
# 이 과정을 K번 반복한다.
# 최종 격자 상태를 출력하라.

def solution(n, k, grid):
    for _ in range(k):
        new_grid = [[0] * n for _ in range(n)]

        for y in reversed(range(n)):
            for x in range(n - 1, -1, -1):
                if grid[y][x] == 1:
                    if 0 <= y + 1 < n and grid[y + 1][x] == 0:
                        new_grid[y + 1][x] = 1
                    else:
                        new_grid[y][x] = 1

        grid = new_grid
    return grid

sol = solution(
    n = 5,
    k = 2,
    grid = [
        [0,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
)
print(sol)
# [
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,0,0,0,0],
#     [0,1,0,0,0],
#     [0,0,1,0,0],
# ]
