# 백준 2606번 바이러스

# 어떤 회사에 여러 대의 컴퓨터가 있고, 일부 컴퓨터들은 네트워크로 연결되어 있어.
# 1번 컴퓨터가 바이러스에 감염되었을 때, 네트워크를 통해 바이러스에 감염되는 컴퓨터가 총 몇 대인지 구하는 문제야.
# 단, 처음부터 바이러스에 걸린 1번 컴퓨터는 정답에 포함하지 않아.

# 첫 번째 줄: 컴퓨터의 개수 N (1 이상 100 이하)
# 두 번째 줄: 네트워크에 직접 연결된 컴퓨터 쌍의 개수 M
# 그다음 M개의 줄: 서로 연결된 컴퓨터 두 대의 번호

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# 4

from collections import defaultdict

n = int(input())
m = int(input())
# graph = defaultdict(list)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

checked = [False] * (n + 1)
answer = []

def dfs(node):
  checked[node] = True
  answer.append(node)

  for nx in graph[node]:
    if not checked[nx]:
      dfs(nx)

dfs(1)
print(len(answer) - 1)
