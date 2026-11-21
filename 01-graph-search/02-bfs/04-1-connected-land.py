# 연결된 땅 덩어리 개수 구하기
# 다음 지도에서 상하좌우로 연결된 1의 영역이 몇 개인지 출력하는 프로그램을 만들어보자.

from collections import deque

graph = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

n, m = len(graph), len(graph[0])
checked = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    checked[y][x] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and not checked[ny][nx]:
                    checked[ny][nx] = True
                    q.append((nx, ny))

count = 0

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not checked[y][x]:
            count += 1
            bfs(x, y)

print(count)  # 2
