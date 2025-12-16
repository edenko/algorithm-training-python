import sys, heapq
input = sys.stdin.readline

def solution(scoville, K):
    cnt = 0
    pq = []
    for i in scoville:
        heapq.heappush(pq, i)

    while pq[0] < K:
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)

        x = first + (second * 2)

        if not pq and x < K:
            return -1

        heapq.heappush(pq, x)

        cnt += 1

    return cnt
    
sol = solution(
    scoville = [1, 2, 3, 9, 10, 12],
    K = 7
)
print(sol) # 2