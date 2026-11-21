# 완전탐색 - 조합/순열 itertools 응용 (combinations/permutations)
from itertools import combinations, permutations

nums = list(map(str, input().split()))

print('조합 : ')
for p in combinations(nums, 2):
    print(p)

print('순열 : ')
for p in permutations(nums, 2):
    print(p)
