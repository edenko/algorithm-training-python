from collections import defaultdict

graph = defaultdict(list)
visited = set()
count = 0

def dfs(new):
    visited.add(new)
    for nxt in graph[new]:
        if nxt not in visited:
            dfs(nxt)

n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in range(1, n + 1):
    if node not in visited:
        count += 1
        dfs(node)

print(count)
