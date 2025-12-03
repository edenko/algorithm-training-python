graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4],
    6: []
}

visited = set()
count = 0

def dfs(new):
    visited.add(new)

    for nxt in graph[new]:
        if nxt not in visited:
            dfs(nxt)


for item in graph:
    if item not in visited:
        count += 1
        dfs(item)

print(count)