# 백준 1927 최소 힙

# 스택과 큐는 들어온 순서에 따라 원소를 꺼냈지? 
# 반면 힙은 우선순위가 높은 원소부터 꺼내는 자료구조야.

# N개의 명령이 주어져. 각 명령은 정수 x야.
# - x > 0이면 힙에 x를 추가해.
# - x == 0이면 힙에서 가장 작은 값을 제거하고 출력해.
# - 힙이 비어 있는데 0이 들어오면 0을 출력해.

# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32

# 0
# 1
# 2
# 12345678
# 0

import heapq

n = int(input())
array = [int(input()) for _ in range(n)]

heap = []

for a in array:
  if a == 0:
    print(heapq.heappop(heap) if heap else 0)
  elif a > 0:
    heapq.heappush(heap, a)
    