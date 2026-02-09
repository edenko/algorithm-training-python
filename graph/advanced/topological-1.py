# 1️⃣ 위상 정렬이란?
# 선후 관계가 있는 작업들을 조건을 만족하게 나열하는 것
# 위상 정렬은 보통 BFS + 진입차수(indegree) 로 푼다.

# 진입차수 = 나에게 들어오는 간선 수
# 진입차수 0 → 지금 당장 실행 가능

# 대표적인 문제
# “선수 과목”
# “먼저 해야 하는 작업”
# “A가 끝나야 B 가능”
# “순서를 정하라”
# “가능한 수행 순서”

# 2️⃣ 알고리즘 흐름 (이걸 외우면 됨)
# 그래프 구성
# 각 노드의 진입차수 계산
# 진입차수 0인 노드를 큐에 넣기
# 큐에서 하나 꺼냄
# 그 노드가 가리키는 노드들의 진입차수 감소
# 새로 0이 되면 큐에 추가
# 큐 빌 때까지 반복

# 문제 1 — 선수 과목 (Topological Sort)
# 대학교에는 1번부터 N번까지 총 N개의 과목이 있다.
# 일부 과목은 선수 과목이 존재한다.

# 과목 A가 과목 B의 선수 과목이라면
# 👉 A를 먼저 이수해야 B를 들을 수 있다.

# 모든 과목을 수강할 수 있도록 가능한 한 가지 수강 순서를 출력하라.

# 4 3
# 1 2
# 1 3
# 3 4

## 1 2 3 4 또는 1 3 4 2

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    x = q.popleft()
    result.append(x)

    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

if len(result) != n:
    print("IMPOSSIBLE")
else:
    print(*result)
