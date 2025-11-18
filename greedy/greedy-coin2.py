# 그리디 - 거스름돈 문제 : 가장 적은 동전 개수로 잔돈

price = 3800
paid = 5000
coins = [500, 100, 50, 10]

change = paid - price
cnt = 0
arr = []

for coin in coins:
    if (change >= coin):
        cnt += change // coin
        change = change % coin
        arr.append((coin, cnt, change))

print(cnt)
print(arr)