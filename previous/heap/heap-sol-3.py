import heapq

def solution(operations):
    answer = []
    n = len(operations)
    op = [list(map(str, x.split())) for x in operations]

    idx = 0
    visited = [False] * n
    min_pq = []
    max_pq = []
    
    for key, value in op:
        if key == 'I':
            heapq.heappush(min_pq, (int(value), idx))
            heapq.heappush(max_pq, (-int(value), idx))
            visited[idx] = True
            idx += 1
            
        elif key == 'D' and value == '1':
            while max_pq:
                v, i = heapq.heappop(max_pq)
                if visited[i]:
                    visited[i] = False
                    break
                
        elif key == 'D' and value == '-1':
            while min_pq:
                v, i = heapq.heappop(min_pq)
                if visited[i]:
                    visited[i] = False
                    break
                
    if not min_pq and not max_pq:
        answer = [0, 0]
    else:
        max_value = 0
        min_value = 0
        while max_pq:
            v, i = heapq.heappop(max_pq)
            if visited[i]:
                max_value = v
                break
        while min_pq:
            v, i = heapq.heappop(min_pq)
            if visited[i]:
                min_value = v
                break
                
        answer = [-max_value, min_value]
    
    return answer

sol = solution(
    operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"] # [0,0]
    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] # [333, -45]
)
print(sol)