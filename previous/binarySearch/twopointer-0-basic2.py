# 📌 문제 2

# 정수 배열 nums가 주어진다.
# 합이 정확히 k가 되는 연속 부분 배열의 개수를 구하라.

# 조건
# nums[i] ≥ 1
# 1 ≤ N ≤ 100,000
# O(N) 풀이 요구

# nums = [1, 2, 1, 2, 1]
# k = 3
## 4 -> [1,2], [2,1], [1,2], [2, 1]

def solution(nums, k):
    l = 0
    total = 0
    cnt = 0

    for r in range(len(nums)):
        total += nums[r]

        while total > k:
            total -= nums[l]
            l += 1
        
        if total == k:
            cnt += 1
        
    return cnt



sol = solution(
    nums = [1, 2, 1, 2, 1],
    k = 3
)
print(sol)
