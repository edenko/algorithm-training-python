# 누적합 + 해시 버전 -> 이해 안됨 넘어감. DAY 11
from collections import defaultdict

def solution(nums, k):
    prefix = 0
    cnt = 0
    mp = defaultdict(int)
    mp[0] = 1

    for x in nums:
        prefix += x
        cnt += mp[prefix - k]
        mp[prefix] += 1
    
    return cnt

sol = solution(
    nums = [1, 2, 1, 2, 1],
    k = 3
)
print(sol) # 4
