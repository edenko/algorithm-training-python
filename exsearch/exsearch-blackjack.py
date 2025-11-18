# 완전탐색 - 블랙잭

from itertools import combinations

n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

best = 0

for combo in combinations(cards, 3):
    total = sum(combo)
    if total <= m:
        best = max(best, total)

print(best)