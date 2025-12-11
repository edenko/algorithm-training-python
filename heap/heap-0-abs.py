import heapq

heap = []
n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(n):
    if nums[i] != 0:
        heapq.heappush(heap, (abs(nums[i]), nums[i]))
    else:
        if not heap:
            print(0)
            continue

        res = heapq.heappop(heap)[1]
        print(res)

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