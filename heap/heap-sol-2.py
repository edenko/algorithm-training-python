import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)

    pq = []
    idx = 0
    time = 0
    count = 0
    answer = 0

    while count < n:

        while idx < n and jobs[idx][0] <= time: # 현재 시간 이하로 요청된 작업을 pq에 넣는다
            req, dur = jobs[idx]
            heapq.heappush(pq, (dur, req))
            idx += 1

        if not pq: # 만약 pq가 비어있다면 → 요청시간까지 time 점프
            time = jobs[idx][0]
            continue

        dur, req = heapq.heappop(pq)
        time += dur
        answer += (time - req) # (현재시간 - 요청시간)
        count += 1

    return answer // n
    
sol = solution(
    # jobs = [[0, 3], [1, 9], [3, 5]] # 8
    jobs = [[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]] # 11
)
print(sol) 