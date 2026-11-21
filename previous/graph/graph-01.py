from collections import deque
from collections import defaultdict

def solution(n, vertex):
    graph = defaultdict(list)

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs():
        checked = [False] * (n + 1)
        dist = [0] * (n + 1)
        q = deque()
        q.append(1)
        checked[1] = True
        
        while q:
            x = q.popleft()

            for nx in graph[x]:
                if not checked[nx]:
                    checked[nx] = True
                    dist[nx] = dist[x] + 1
                    q.append(nx)
        
        return dist

    result = bfs()
    return result.count(max(result)) # 3

sol = solution(
    n = 6,
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
)

print(sol) 
