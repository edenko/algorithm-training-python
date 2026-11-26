# 백준 11000 강의실 배정

# 3
# 1 3
# 2 4
# 3 5

# 2

# 4
# 1 2
# 1 3
# 2 5
# 3 4

# 2

import heapq

n = int(input())
array = []
rooms = []

for _ in range(n):
  a, b = map(int, input().split())
  array.append((a, b))

array = sorted(array, key=lambda x: (x[0], x[1]))

for start, end, time in array:

  if rooms and rooms[0] <= start:
    heapq.heappop(rooms)

  heapq.heappush(rooms, end)

print(len(rooms))
