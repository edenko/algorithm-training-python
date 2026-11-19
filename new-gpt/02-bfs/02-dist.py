# bfs(start) 함수를 만들고 다음을 만족하도록 구현해봐.
# - deque 사용하기
# - 시작 노드의 거리는 0
# - 아직 발견하지 않은 노드의 거리는 -1
# - 이웃 노드를 처음 발견할 때 거리 계산하기
# - 모든 노드까지의 최단 거리를 리스트로 반환하기
# - visited 배열 없이 dist만 사용하기
# 이번 문제는 완성된 DFS 코드가 아니라 BFS에 거리 계산 기능을 추가하는 연습이야.

from collections import deque

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

def bfs(start):
  q = deque([start])
  dist = [-1] * len(graph)
  dist[start] = 0

  while q:
    node = q.popleft()

    for nx in graph[node]:
      if dist[nx] == -1:
        dist[nx] = dist[node] + 1
        q.append(nx)

  return dist

print(bfs(1))
