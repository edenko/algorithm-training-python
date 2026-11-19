# 문제: 그래프의 DFS 방문 순서 출력

# 주어진 양방향 그래프에서 1번 노드부터 DFS 탐색을 시작해. 방문한 노드 번호를 방문 순서대로 출력하는 함수를 작성해봐.

# 조건은 다음과 같아.
# - 스택을 사용하는 반복문 DFS로 구현할 것
# - visited 배열을 사용할 것
# - 방문 처리는 스택에서 노드를 꺼낼 때 할 것
# - 항상 번호가 작은 이웃 노드를 먼저 방문할 것
# - 이미 방문한 노드는 다시 출력하지 않을 것

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 6],
    [2],
    [2],
    [3]
]

visited = [False] * len(graph)

def dfs(start):
  stack = [start]
  answer = []

  while stack:
    node = stack.pop()

    if visited[node]:
      continue

    visited[node] = True
    stack.extend(sorted(graph[node], reverse=True))
    answer.append(node)

  return answer

print(dfs(1))
