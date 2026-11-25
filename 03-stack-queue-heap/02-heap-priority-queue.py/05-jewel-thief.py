# 백준 1202 보석 도둑

# N개의 보석과 K개의 가방이 있어.
# 각 보석에는 무게 M과 가격 V가 있고, 각 가방에는 최대 수용 무게 C가 있어.

# 조건은 다음과 같아.
# - 가방 하나에는 보석을 최대 1개만 넣을 수 있어.
# - 보석 하나는 한 번만 사용할 수 있어.
# - 보석 무게는 가방의 수용 무게 이하여야 해.
# - 가져갈 수 있는 보석 가격의 합을 최대화해야 해.

# N과 K는 각각 최대 300,000이므로 모든 가방과 보석을 이중 반복문으로 비교하는 방식은 비효율적이야

# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2

# 164

import heapq

n, m = map(int, input().split())
jewels = []
bags = []
answer = 0

for _ in range(n):
  weight, price = map(int, input().split())
  jewels.append((weight, price))
jewels.sort()

for _ in range(m):
  bags.append(int(input()))
bags.sort()

heap = []
idx = 0

for bag in bags:
  while idx < n and jewels[idx][0] <= bag:
    weight, price = jewels[idx]
    heapq.heappush(heap, -price)

    idx += 1

  if heap:
    answer += -heapq.heappop(heap)

print(answer)
