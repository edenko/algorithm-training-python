# 백준 2503 숫자 야구

# 영수가 1부터 9까지의 서로 다른 숫자 3개로 세 자리 수를 만들었어.
# 민혁이가 숫자를 추측하면 영수는 스트라이크와 볼의 개수를 알려줘.

# - 스트라이크(S): 숫자와 위치가 모두 일치
# - 볼(B): 숫자는 포함되어 있지만 위치가 다름
# - 아웃: 일치하는 숫자가 없음

# 질문과 답변 기록이 주어질 때, 
# 영수가 생각한 숫자로 가능한 세 자리 수가 총 몇 개인지 구해야 해.

# n = 횟수
# 질문한 숫자, 스트라이크 수, 볼 수

# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1

# 2

n = int(input())
graph = []
path = []
checked = [False] * 10
qu = []
answer = 0

for i in range(n):
  num, strike, ball = map(int, input().split())
  qu.append((str(num), strike, ball))

def dfs():
  if len(path) == 3:
    string = ''
    for p in path:
      string += str(p)
    graph.append(string)
    return

  for i in range(1, 10):
    if not checked[i]:
      checked[i] = True
      path.append(i)

      dfs()

      path.pop()
      checked[i] = False

dfs()

for candidate in graph:
  failed = False
  for num, strike, ball in qu:
    s = 0
    b = 0

    for i in range(3):
      if num[i] == candidate[i]:
        s += 1
      elif num[i] in candidate:
        b += 1

    if s != strike or b != ball:
      failed = True
      break

  if not failed: 
    answer += 1

print(answer)
