# 스택/큐 - 기능개발
import math

progresses = [85, 80, 90, 85]
speeds = [5, 5, 5, 5]
answer = []

remain = []
for idx, item in enumerate(progresses):
    res = math.ceil((100 - item) / speeds[idx])
    remain.append(res)
    
prev = remain[0]
cnt = 1
for item in remain[1::]:
    if (prev != 0 and prev < item):
        answer.append(cnt)
        cnt = 0
        
    prev = item
    cnt += 1
    
answer.append(cnt)
print(answer)

