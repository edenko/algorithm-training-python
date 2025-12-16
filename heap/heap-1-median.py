# 7
# 1
# 5
# 2
# 10
# 3
# 12
# 8

## 1
## 1
## 2
## 2
## 3
## 3
## 5

# 중앙값 유지 (Running Median) (구현)

# 정수가 한 개씩 들어온다.
# 매 숫자가 들어올 때마다 현재까지의 숫자들의 중앙값을 출력하라.

# 중앙값 정의:
# 수의 개수가 홀수 → 중앙에 있는 값
# 수의 개수가 짝수 → 두 중앙 중 작은 값을 출력한다. (코테 표준 규칙)

import sys, heapq
input = sys.stdin.readline

n = int(input())

minh = []
maxh = []

for _ in range(n):
    x = int(input())

    heapq.heappush(maxh, -x)

    if minh and (minh[0] < -maxh[0]):
        big = -heapq.heappop(maxh)
        small = heapq.heappop(minh)
        heapq.heappush(maxh, -small)
        heapq.heappush(minh, big)
    
    if len(maxh) > len(minh) + 1:
        heapq.heappush(minh, -heapq.heappop(maxh))

    if len(maxh) < len(minh):
        heapq.heappush(maxh, -heapq.heappop(maxh))

    print(maxh[0])
