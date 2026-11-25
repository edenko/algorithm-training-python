import heapq

n, m = map(int, input().split())
jewels = []
bags = []
answer = 0

for i in range(n):
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