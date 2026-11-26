# 백준 2294 동전 2

# n가지 종류의 동전이 있다. 
# 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 
# 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 
# 각각의 동전은 몇 개라도 사용할 수 있다.

# 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 
# 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 
# 동전의 가치는 100,000보다 작거나 같은 자연수이다. 
# 가치가 같은 동전이 여러 번 주어질 수도 있다.

# 3 15
# 1
# 5
# 12

# 3

n, target = map(int, input().split())
coins = []

for _ in range(n):
  coins.append(int(input()))

INF = float('inf')
dp = [INF] * (target + 1)
dp[0] = 0

for i in range(1, target + 1):

  count = INF
  for coin in coins:
    if i - coin >= 0:
      count = min(count, dp[i - coin] + 1)

  dp[i] = count

print(dp[target] if dp[target] != INF else -1)
