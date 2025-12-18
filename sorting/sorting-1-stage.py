# 실패율 정렬

# 1번부터 N번까지 스테이지가 있다

# 각 사용자의 현재 스테이지가 주어진다

# 실패율 = (해당 스테이지에 머물러 있는 사람 수) / (도달한 사람 수)

# 👉 실패율이 높은 스테이지부터 정렬하라
# 👉 실패율이 같으면 스테이지 번호가 작은 것부터

from collections import Counter

def solution(stages, n):
    answer = []
    cnt = Counter(stages)
    users = len(stages)

    for i in range(1, n + 1):
        stay = cnt[i]
        fail = stay / users if users > 0 else 0
        answer.append((i, fail))
        users -= stay

    answer.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in answer]

sol = solution(
    stages = [2,1,2,6,2,4,3,3],
    n = 5
)
print(sol) # [3, 4, 2, 1, 5]
