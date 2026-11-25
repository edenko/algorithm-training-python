# 백준 2075 N번째 큰 수

# N×N의 표에 수 N2개 채워져 있다. 
# 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다.

# 5
# 12 7 9 15 5
# 13 8 11 19 6
# 21 10 26 31 16
# 48 14 28 35 25
# 52 20 32 41 49

# 35

import heapq

n = int(input())
heap = []

for _ in range(n):
  array = list(map(int, input().split()))
  for a in array:
    heapq.heappush(heap, a)

    if len(heap) > n:
      heapq.heappop(heap)

print(heapq.heappop(heap))
