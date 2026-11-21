# 3  
# 3   1 4 7
# 4   2 5 6 8
# 2   0 9

## 0 1 2 4 5 6 7 8 9

# 여러 개의 정렬 배열을 하나로 합치기 (K-way Merge)

# 📌 문제 설명
# K개의 정렬된 리스트가 있다.
# 이 리스트들을 하나의 정렬된 리스트로 병합하라.

# 모든 리스트의 총 원소 수 N은 1,000,000까지 가능하다.

# 정렬로 해결 금지
# (O(N log N)) → 통과 못함.
# 힙 사용 필수
# O(N log K)로 해결해야 한다.

import sys, heapq
input = sys.stdin.readline

n = int(input())
lists = [list(map(int, input().split())) for _ in range(n)]

pq = []

for i in range(n):
    length = lists[i][0]
    values = lists[i][1:]
    lists[i] = values

    if length > 0:
        heapq.heappush(pq, (lists[i][0], i, 0))


result = []
while pq:
    x, li, idx = heapq.heappop(pq)
    result.append(x)

    if idx + 1 < len(lists[li]):
        heapq.heappush(pq, (lists[li][idx + 1], li, idx + 1))

print(result)

