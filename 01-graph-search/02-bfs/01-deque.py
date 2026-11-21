# 1번 노드에서 BFS를 시작해서 방문한 노드의 순서를 리스트로 반환하는 함수를 작성해봐.

# 구현 조건
# - deque를 사용하기
# - bfs(start) 함수 만들기
# - 방문 배열 visited 사용하기
# - 시작 노드는 큐에 넣을 때 방문 처리하기
# - 이웃 노드는 미방문 상태일 때만 큐에 넣기
# - 방문한 노드의 순서를 answer 리스트에 저장하기
# - answer를 반환하기

from collections import deque

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6, 7],
    [2],
    [2],
    [3],
    [3]
]

def bfs(start):
  q = deque([start])
  checked = [False] * len(graph)
  checked[start] = True
  answer = []

  while q:
    node = q.popleft()
    answer.append(node)

    for nx in graph[node]:
      if not checked[nx]:
        q.append(nx)
        checked[nx] = True

  return answer

print(bfs(1))
