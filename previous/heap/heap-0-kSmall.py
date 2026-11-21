# 배열에서 K번째로 작은 수 찾기

import heapq

heap = []
nums = [7, 10, 4, 3, 20, 15]
K = 3

for x in nums:
    heapq.heappush(heap, -x)
    if len(heap) > 3:
        heapq.heappop(heap)
    
print(-heapq.heappop(heap)) # 7
