# 바이러스 (BOJ 2606)
# 1번 컴퓨터와 직접 또는 간접적으로 연결된 모든 컴퓨터는 감염된다..

# 👉 1번 컴퓨터를 제외하고,
# 👉 감염되는 컴퓨터 수를 출력하라.

# 7 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

## 4

from collections import defaultdict
graph = {}
visited = set()
count = [0]

def dfs(new):
    visited.add(new)
    count[0] += 1

    for nxt in graph[new]:
        if nxt not in visited:
            dfs(nxt)

n, m = map(int, input().split())
graph = defaultdict(list)
for a, b in (map(int, input().split()) for _ in range(m)):
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(count[0] - 1)