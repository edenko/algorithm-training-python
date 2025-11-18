# 그리디 - 동전 교환 최소 개수 (Greedy 응용) : 정확한 목표 금액

n = 6
coins = [1, 5, 10, 50, 100, 500]
k = 4720
coins.sort(reverse=True)
total = 0
arr = []

for coin in coins:
    cnt = k // coin
    total += cnt
    k = k % coin
    arr.append((coin, cnt))

print(total, arr)
