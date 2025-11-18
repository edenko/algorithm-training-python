# 그리디 - 동전 최소 갯수로 금액 채우기

K = 4200
coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
result = []

coins.sort(reverse=True)

for coin in coins:
    if (K >= coin):
        cnt = K // coin
        K = K % coin
        result.append((coin, cnt))

print(result)