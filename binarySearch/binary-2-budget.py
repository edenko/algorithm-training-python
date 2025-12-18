# 예산 배정 (상한선 이분탐색)

# 여러 지방의 예산 요청이 있다.
# 총 예산이 M으로 정해져 있을 때,

# 각 지방에는 요청한 금액 그대로 주되,
# 총합이 M을 넘으면 상한선(cap) 을 정해서
# 각 지방에는 min(요청, cap) 만큼만 배정한다.

# 👉 총합이 M을 넘지 않도록 하는 최대 상한선(cap) 을 구하라.

# ✔ 조건
# budgets: 각 지방의 요청 예산 (정수 배열)
# M: 총 예산
# 1 ≤ len(budgets) ≤ 100,000

def solution(budgets, m):
    answer = 0
    l, r = 0, max(budgets)

    def check(mid):
        total = 0
        for x in budgets:
            total += min(x, mid)
        return total <= m

    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
            
    return answer

sol = solution(
    budgets = [120, 110, 140, 150],
    m = 485
)
print(sol) # 127
