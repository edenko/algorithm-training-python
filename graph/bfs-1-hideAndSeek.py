# 5 17
# **1차원 선(line)**에서 이동
from collections import deque

n, k = map(int, input().split())
MAX = 100000
checked = [False] * (MAX + 1)
dist = [0] * (MAX + 1)

def bfs(start):
    q = deque()
    q.append(start)
    checked[start] = True

    while q:
        x = q.popleft()

        if x == k:
            return dist[x]
        
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX:
                if not checked[nx]:
                    checked[nx] = True
                    dist[nx] = dist[x] + 1
                    q.append(nx)

print(bfs(n)) # 4
