# 깊이/너비 우선 탐색(DFS/BFS)
# 퍼즐 조각 채우기

from collections import deque

def solution(game_board, table):
    n = len(game_board)
    answer = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # BFS로 블럭 추출
    def bfs(x, y, v, board, visited):
        q = deque([(x, y)])
        visited[y][x] = True
        result = [(x, y)]

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[ny][nx] and board[ny][nx] == v:
                        visited[ny][nx] = True
                        result.append((nx, ny))
                        q.append((nx, ny))
        return result

    # 정규화
    def normalize(block):
        min_x = min([x for x, y in block])
        min_y = min([y for x, y in block])
        new_block = sorted([(x - min_x, y - min_y) for x, y in block])
        return new_block

    # 회전
    def rotate(block):
        rotated = [(y, -x) for x, y in block]
        return normalize(rotated)

    # 빈칸(0), 퍼즐(1) 모양 추출
    game_blocks = []
    table_blocks = []

    visited_game = [[False]*n for _ in range(n)]
    visited_table = [[False]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0 and not visited_game[y][x]:
                block = bfs(x, y, 0, game_board, visited_game)
                game_blocks.append(normalize(block))
            if table[y][x] == 1 and not visited_table[y][x]:
                block = bfs(x, y, 1, table, visited_table)
                table_blocks.append(normalize(block))

    # 매칭 시도
    used = [False] * len(table_blocks)

    for game in game_blocks:
        for i in range(len(table_blocks)):
            if used[i]: 
                continue
            block = table_blocks[i]
            if len(block) != len(game): 
                continue

            current = block[:]
            match = False
            for _ in range(4):
                if current == game:
                    match = True
                    break
                current = rotate(current)

            if match:
                used[i] = True
                answer += len(game)
                break

    return answer

sol = solution(
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
)

print(sol)
