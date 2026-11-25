# 프린터에 여러 개의 문서가 대기하고 있어. 각 문서에는 중요도가 지정돼 있어.

# 프린터는 다음 규칙대로 동작해.
# 1. 대기열 맨 앞의 문서를 확인한다.
# 2. 대기열에 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 현재 문서를 맨 뒤로 보낸다.
# 3. 그렇지 않으면 현재 문서를 인쇄하고 대기열에서 제거한다.

# 우리가 알아내야 할 것은 **처음에 M번째 위치에 있던 문서가 몇 번째로 인쇄되는가?**야.
# 위치는 0부터 시작해.

# 첫 줄에 테스트케이스의 수가 주어진다. 
# 각 테스트케이스는 두 줄로 이루어져 있다.
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 
# 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 
# 이때 맨 왼쪽은 0번째라고 하자. 
# 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# 1
# 2
# 5

from collections import deque

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  priorities = list(map(int, input().split()))

  q = deque()
  for i in range(len(priorities)):
    q.append((i, priorities[i]))

  cnt = 1
  while q:
    idx, num = q.popleft()

    if any(num < priority for _, priority in q):
      q.append((idx, num))
    else:
      if idx == m:
        print(cnt)
        break

      cnt += 1