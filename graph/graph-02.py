from collections import deque, defaultdict

def solution(n, results):
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    answer = 0

    def bfs(start, graph):
        q = deque()
        q.append(start)
        checked = [False] * (n + 1)
        checked[start] = True
        cnt = 0

        while q:
            x = q.popleft()

            for nx in graph[x]:
                if not checked[nx]:
                    checked[nx] = True
                    q.append(nx)
                    cnt += 1
        return cnt

    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)

    for i in range(1, n + 1):
        win = bfs(i, win_graph)
        lose = bfs(i, lose_graph)

        if win + lose == n - 1:
            answer += 1
    
    return answer

sol = solution(
    n = 5,
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
)

print(sol)
