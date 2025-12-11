import heapq

def solution(jobs):
    answer = 0
    cnt = 0
    pq = []
    arr = []
    
    for i in range(len(jobs)):
        s, l = jobs[i]
        heapq.heappush(pq, (l, s, i))
    
    while pq:
        s, l, i = heapq.heappop(pq)
        cnt += s
        answer += (cnt - l)

    return answer // len(jobs)
    
sol = solution(
    jobs = [[0, 3], [1, 9], [3, 5]]
)
print(sol) # 8