# 백준 2493 탑

# 일직선 위에 N개의 탑이 서 있어.
# 각 탑은 왼쪽 방향으로 레이저 신호를 보내고, 
# 신호는 자신보다 높이가 크거나 같은 탑을 만나면 그 탑에 수신돼.
# 각 탑의 레이저를 처음으로 수신하는 탑의 번호를 출력해야 해.

# 수신하는 탑이 없다면 0을 출력해.
# 입력 조건
# - 탑의 개수 N: 1 이상 500,000 이하
# - 탑 높이: 1 이상 100,000,000 이하
# - 탑 번호는 왼쪽부터 1번으로 시작해.

# 5
# 6 9 5 7 4

# 0 0 2 2 4

# 3
# 5 5 5 

# 0 1 2

n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

idx = 0
for tower in towers:
  new_idx = 0
  while stack:
    prev_tower, prev_idx = stack[-1]

    if prev_tower >= tower:
      new_idx = prev_idx
      break
    else:
      stack.pop()

  answer.append(new_idx)
  stack.append((tower, idx + 1))
  idx += 1

# print(*answer)
print(' '.join(map(str, answer)))
