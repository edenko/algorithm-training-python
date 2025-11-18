# 그리디 - 회의실 배정 2 : 최소 몇 개의 회의실이 필요한가? (우선순위 큐 - heapq)
# 시작 시간을 기준으로 정렬해야됨
import heapq

n = 5
meetings = [
    (1, 4),
    (2, 5),
    (9, 10),
    (6, 8),
    (3, 6)
]

meetings.sort(key=lambda x: (x[0], x[1]))
rooms = [meetings[0][1]]
heapq.heapify(rooms)

for start, end in meetings[1:]:
    if (rooms[0] <= start):
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)

print(len(rooms))


