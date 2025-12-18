# 작업 처리 / 생산량 (속도 파라메트릭)

# 여러 작업이 있다.
# 각 작업은 정해진 작업량을 가지고 있고,
# 너는 일정한 속도(speed) 로 작업을 처리한다.

# 👉 모든 작업을 제한 시간 H 안에 끝낼 수 있는
# 최소 속도(speed) 를 구하라.

# ✔ 조건
# works: 각 작업의 작업량 (정수 배열)
# H: 제한 시간
# 한 작업은 쪼갤 수 없음
# 작업은 순차가 아니라 독립적 (각각 시간 계산)

import math
def solution(works, h):
    answer = 0
    l, r = 1, max(works)

    def check(mid):
        time = 0
        for work in works:
            time += math.ceil(work / mid)
        return time <= h

    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer

sol = solution(
    works = [3, 6, 7, 11],
    h = 8
)
print(sol) # 4
