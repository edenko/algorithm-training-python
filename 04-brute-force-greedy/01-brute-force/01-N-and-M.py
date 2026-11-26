# 백준 15649 N과 M (1)

# 정수 N과 M이 주어졌을 때, 
# 1부터 N까지 서로 다른 자연수 M개를 선택해 만들 수 있는 모든 순열을 출력하는 문제야.

# 입력은 N M이고, 1 ≤ M ≤ N ≤ 8이야.

# 3 2

# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2

n, m = map(int, input().split())
path = []
checked = [False] * (n + 1)

def dfs():
  if len(path) == m:
    print(*path)
    return
  
  for i in range(1, n + 1):
    if not checked[i]:
      checked[i] = True
      path.append(i)

      dfs()

      path.pop()
      checked[i] = False

dfs()
