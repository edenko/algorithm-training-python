# 백준 15649번 N과 M (1) 
# - 조건을 만족하는 모든 경우를 찾아내는 문제

# 자연수 N과 M이 주어져.
# 1부터 N까지의 자연수 중에서 서로 다른 M개의 숫자를 골라 만들 수 있는 모든 수열을 출력

# 규칙은 다음과 같아.
# - 사용할 수 있는 숫자는 1부터 N까지야.
# - 수열 하나에는 숫자가 정확히 M개 들어가야 해.
# - 하나의 수열 안에서는 같은 숫자를 두 번 사용할 수 없어.
# - 숫자의 순서가 달라지면 서로 다른 수열이야.
# - 결과는 사전순으로 증가하는 순서로 출력해야 해.
# 입력 조건은 1 ≤ M ≤ N ≤ 8이야.

# 3 1

# 1
# 2
# 3

# 4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

n, m = map(int, input().split())
path = []
checked = [False] * (n + 1)

def dfs():

  if len(path) == m:
    print(*path)
    return

  for i in range(1, n + 1):
    if not checked[i]: # 중복 제거 코드 (1 1 같은)
      checked[i] = True
      path.append(i)

      dfs()

      path.pop()
      checked[i] = False

dfs()
