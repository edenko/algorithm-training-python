# **1차원 선(line)**에서 이동
# 숨바꼭질 (BOJ 1697)

# 수빈이는 현재 위치 N에 있고, 동생은 위치 K에 있다.
# 수빈이는 1초마다 다음 중 하나의 행동을 할 수 있다.

# x → x - 1
# x → x + 1
# x → 2 * x

# 👉 **수빈이가 동생을 찾는 가장 빠른 시간(최소 초)**을 구하라.

# 5 17
## 4

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
