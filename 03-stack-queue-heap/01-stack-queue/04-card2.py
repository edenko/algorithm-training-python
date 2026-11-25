# 백준 2164 카드2

# 1부터 N까지 번호가 적힌 카드가 있어. 
# 처음에는 1번 카드가 맨 위, N번 카드가 맨 아래에 놓여 있어.

# 카드가 한 장 남을 때까지 아래 동작을 반복해.
# 1. 맨 위의 카드를 버린다.
# 2. 그다음 맨 위의 카드를 맨 아래로 옮긴다.
# 마지막에 남는 카드의 번호를 출력해야 해.

# - 첫 번째 줄에 정수 N이 주어져.
# - 1 ≤ N ≤ 500,000

# 6

# 4

from collections import deque

n = int(input())
q = deque()

for i in range(1, n + 1):
  q.append(i)

while len(q) > 1:
  q.popleft()
  q.append(q.popleft())

print(q[0])