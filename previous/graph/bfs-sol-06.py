# 깊이/너비 우선 탐색(DFS/BFS)
# 여행경로

from collections import defaultdict, deque

def solution(tickets):
    graph = defaultdict(list)
    route = []

    def dfs(node):
        print('===========================')
        while graph[node]:
            print(node)
            print(graph[node])
            # dfs(graph[node].pop(0))
            dfs(graph[node].popleft())
        route.append(node) # 멀리 있는 순서대로 출력함
        print(route)

    for start, end in tickets:
        graph[start].append(end)
        
    print(graph)
    for k in graph:
        # graph[k].sort(reverse=True)
        graph[k] = deque(sorted(graph[k]))
    
    print(graph)
    dfs('ICN')

    return route[::-1]

sol = solution(
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
)

print(sol)
