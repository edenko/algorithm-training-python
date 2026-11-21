# ‘절댓값 힙’ (BOJ 11286)

# 입력값이 0이 아니면 해당 숫자를 자료구조에 추가
# 입력값이 0이면 자료구조에서 절댓값이 가장 작은 값을 출력하고 제거

# 만약 절댓값이 같다면 → 실제 값이 더 작은 수를 출력
# (예: -1 과 1 → -1 출력)

# 자료구조가 비어 있으면 0 출력

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