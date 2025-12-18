# 문제 1: 입국 심사 (기업 코테 최빈)
# 📌 문제 설명

# N명의 사람이 입국 심사를 기다리고 있다.
# 각 심사관은 한 사람을 심사하는 데 걸리는 시간이 다르다.

# 모든 사람이 심사를 받는 데 걸리는 최소 시간을 구하라.

# ✔ 조건
# times: 심사관별 소요 시간 배열
# n: 사람 수
# 1 ≤ len(times) ≤ 100,000
# 1 ≤ n ≤ 1,000,000,000

# 이 시간 안에 

def solution(times, n):
    l, r = 1, max(times) * n
    answer = 0

    def check(mid):
        cnt = 0
        for t in times:
            cnt += mid // t
        return cnt >= n

    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer

sol = solution(
    times = [7, 10],
    n = 6
)
print(sol) # 28
