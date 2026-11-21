# 그래프에서 1번부터 출발해 재귀 DFS를 이용해 방문 순서를 반환하는 함수를 작성해보자.

# 구현 조건
# - dfs(node) 함수를 재귀적으로 구현하기
# - 방문한 노드는 visited에 기록하기
# - 노드 번호가 작은 이웃부터 방문하기
# - 방문한 순서를 answer에 저장하기
# - 반복문 DFS에서 사용했던 별도의 stack 리스트는 사용하지 않기
# 이 그래프의 인접 리스트는 이미 작은 번호부터 정렬되어 있어.

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

visited = [False] * 7
answer = []

def dfs(node):
  visited[node] = True
  answer.append(node)

  for nx in graph[node]:
    if not visited[nx]:
      dfs(nx)

dfs(1)
print(answer)
