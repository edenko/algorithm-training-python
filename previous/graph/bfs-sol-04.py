# 깊이/너비 우선 탐색(DFS/BFS)
# 아이템 줍기

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 101
    board = [[0] * MAX for _ in range(MAX)]

    # Step 1. 사각형 전체 영역 1로 채우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                board[y][x] = 1

    # Step 2. 내부를 0으로 덮어서 테두리만 남기기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
        for y in range(y1 + 1, y2):
            for x in range(x1 + 1, x2):
                board[y][x] = 2

    # BFS
    q = deque()
    q.append((characterY * 2, characterX * 2, 0))  # ✅ (y, x, dist)
    visited = [[False] * MAX for _ in range(MAX)]
    visited[characterY * 2][characterX * 2] = True

    # 4방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        y, x, d = q.popleft()

        # 도착
        if y == itemY * 2 and x == itemX * 2:
            return d // 2  # 2배 좌표 보정

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < MAX and 0 <= ny < MAX:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx, d + 1))

    return 0


sol = solution(
    [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],
    1,
    3,
    7,
    8
)

print(sol)
