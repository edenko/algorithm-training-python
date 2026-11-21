# 백준 1697번 숨바꼭질

# 수빈이는 위치 N에 있고, 동생은 위치 K에 있어.

# 수빈이는 1초마다 다음 세 가지 행동 중 하나를 할 수 있어.
# - 현재 위치가 x라면 x - 1로 이동
# - 현재 위치가 x라면 x + 1로 이동
# - 현재 위치가 x라면 2 * x로 순간이동
# 동생이 있는 위치 K에 도착하기까지 걸리는 최소 시간을 구하는 문제야.

# 입력으로 N과 K가 주어지고, 둘 다 0 이상 100,000 이하의 정수야.

# 5 17

# 4

from collections import deque

start, finish = map(int, input().split())

def bfs(start):
  q = deque([start])
  dist = [-1] * 100001
  dist[start] = 0

  while q:
    node = q.popleft()

    if node == finish:
      return dist[node]
    
    for nx in [node - 1, node + 1, 2 * node]:
      if 0 <= nx < 100001:
        if dist[nx] == -1:
          dist[nx] = dist[node] + 1
          q.append(nx)

print(bfs(start))
