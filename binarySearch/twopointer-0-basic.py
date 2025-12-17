# DAY 11 — 투포인터 / 슬라이딩 윈도우
# 투포인터란?

# 정렬된 배열 or 연속 구간에서
# 포인터 2개(l, r)를 이동시키며 조건을 만족하는 구간을 찾는 기법

# 시간복잡도: O(N)

# 언제 쓰나?
# 연속 부분 배열
# 합 / 길이 / 개수
# “최대 / 최소”
# “조건을 만족하는 가장 긴(짧은) 구간”


# 📌 문제 1

# 정수 배열 nums와 정수 k가 주어진다.
# 합이 k 이하인 연속 부분 배열 중 가장 긴 길이를 구하라.

# 조건
# 1 ≤ len(nums) ≤ 100,000
# nums[i] ≥ 1 (양수만 존재)
# O(N²) ❌ / O(N) ✔

# nums = [1, 2, 3, 4, 5]
# k = 7
## 3

def solution(nums, k):
    l = 0
    cur = 0

    for i in range(len(nums)):
        cur += nums[i]

        if cur < k:
            l += 1
        else:
            return l


sol = solution(
    nums = [1, 2, 3, 4, 5],
    k = 7
)
print(sol)
