# 백준 15650번 N과 M (2)

# 자연수 N과 M이 주어져.
# 1부터 N까지의 자연수 중에서 서로 다른 M개의 숫자를 골라 수열을 만들어야 해.

# 조건은 다음과 같아.
# 1. 숫자는 1부터 N까지 사용할 수 있어.
# 2. 하나의 수열에서 같은 숫자를 두 번 사용할 수 없어.
# 3. 숫자는 반드시 오름차순이어야 해.
# 4. 조건을 만족하는 모든 수열을 사전순으로 출력해야 해.
# 입력 범위는 1 ≤ M ≤ N ≤ 8이야.

# 4 2

# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# 3 3

# 1 2 3

n, m = map(int, input().split())
path = []
checked = [False] * (n + 1)

def dfs(x):
  if len(path) == m:
    print(*path)
    return

  for i in range(x, n + 1):
    if not checked[i]:
      checked[i] = True
      path.append(i)

      # dfs(i) # 이전 순서를 다시 호출하지 않게 -> i는 checked True라서 건너뜀
      dfs(i + 1)

      path.pop()
      checked[i] = False

dfs(1)
