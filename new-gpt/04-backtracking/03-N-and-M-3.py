# 백준 15651번 · N과 M (3)

# 자연수 N과 M이 주어져.
# 1부터 N까지의 자연수 중에서 M개의 숫자를 선택해 만들 수 있는 모든 수열을 출력해야 해.

# 조건은 다음과 같아.
# - 숫자는 1부터 N까지 사용할 수 있어.
# - 수열의 길이는 정확히 M이어야 해.
# - 같은 숫자를 여러 번 선택해도 돼.
# - 숫자의 순서는 자유야.
# - 모든 수열을 사전순으로 출력해야 해.
# 입력 조건은 1 ≤ M ≤ N ≤ 7이야.

# 2 2

# [[1, 1], [1, 2], [2, 1], [2, 2]]

n, m = map(int, input().split())
path = []
answer = []

def dfs():

  if len(path) == m:
    answer.append(path[:])
    return

  for i in range(1, n + 1):
    path.append(i)

    dfs()

    path.pop()

dfs()

print(answer)
