# DP - 1, 2, 3 더하기

n = 5

dp = [0] * (n + 1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

print(dp[n])
