# 5 4
# 1 3
# 2 3
# 3 4
# 2 5

## 1 2 3 4 5

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

pq = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

result = []

while pq:
    x = heapq.heappop(pq)
    result.append(x)

    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            heapq.heappush(pq, nx)

if len(result) != n:
    print("IMPOSSIBLE")
else:
    print(result) # 1 2 3 4 5