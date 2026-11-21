# 배열 회전 시뮬레이션 (기본 → 실전)

# N×N 정수 배열이 주어진다.
# 이 배열을 시계 방향으로 90도 회전하라.
# 회전은 한 번만 수행한다.
# 회전된 결과 배열을 반환하라.

# 시계 90도 회전
# (old_y, old_x) → (new_y, new_x)
# new_y = x
# new_x = n - 1 - y

def solution(n, grid):
    new_grid = [[0] * n for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            new_grid[x][n - 1 - y] = grid[y][x]

    return new_grid

sol = solution(
    n = 3,
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(sol)
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]