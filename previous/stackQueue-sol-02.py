# 스택/큐 - 프로세스
from collections import deque
# priorities = [2, 1, 3, 2]
priorities = [1, 1, 9, 1, 1, 1]
location = 0

q = deque((p, idx) for idx, p in enumerate(priorities))
order = 0

while q:
    item, idx = q.popleft()
    if any(item < top for top, _ in q):
        q.append((item, idx))
        continue

    order += 1
    if idx == location:
        print(order)
        break
