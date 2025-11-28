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