# 그리디 - 회의실

n = 5
meetings = [
    (1, 4),
    (3, 5),
    (0, 6),
    (5, 7),
    (8, 9)
]

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for start, end in meetings:
    if (start > end_time):
        cnt += 1
        end_time = end

print(cnt)