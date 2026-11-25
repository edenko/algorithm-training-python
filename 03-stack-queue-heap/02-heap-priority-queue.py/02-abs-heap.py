# 백준 11286 절댓값 힙

# 정수 x가 주어질 때마다 다음 작업을 수행해야 해.
# - x != 0 : 정수 x를 힙에 추가
# - x == 0 : 절댓값이 가장 작은 정수를 꺼내서 출력
# - 절댓값이 같다면 실제 값이 더 작은 정수를 먼저 출력
# - 힙이 비어 있다면 0 출력

# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0

# -1
# 1
# 0
# -1
# -1
# 1
# 1
# -2
# 2
# 0

import heapq

n = int(input())
heap = []

for i in range(n):
  x = int(input())

  if x == 0:
    if not heap:
      print(0)
    else:
      a, b = heapq.heappop(heap)
      print(b)
  else:
    heapq.heappush(heap, (abs(x), x))
