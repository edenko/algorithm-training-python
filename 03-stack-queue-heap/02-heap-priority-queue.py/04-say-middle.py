# 백준 1655 가운데를 말해요

# 정수 N개가 한 줄에 하나씩 주어져.
# 숫자가 입력될 때마다 지금까지 입력된 숫자들의 중앙값을 출력해야 해.
# 단, 숫자가 짝수 개라면 중앙에 있는 두 숫자 중 작은 값을 출력해.
# 입력 조건은 N ≤ 100,000, 각 정수는 -10,000 이상 10,000 이하야.

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5

# 1
# 1
# 2
# 2
# 2
# 2
# 5

import heapq

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
  x = int(input())

  if min_heap and x > min_heap[0]:
    heapq.heappush(max_heap, -heapq.heappop(min_heap))
    heapq.heappush(min_heap, x)
  else:
    heapq.heappush(max_heap, -x)

  if i % 2 != 0:
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

  print(-max_heap[0])
  