# DP - 1, 2, 3 더하기 2
# 2차원 DP 확장판(연속 금지)
# give up.....

n = 5

dp = [ [0] * 4 for _ in range(n + 1) ]

dp[1][1], dp[1][2], dp[1][3] = 1, 0, 0
dp[2][1], dp[2][2], dp[2][3] = 0, 1, 0
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, n + 1):
    dp[i][1] = dp[i - 1][2] + dp[i - 1][3]
    dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
    dp[i][3] = dp[i - 1][1] + dp[i - 1][2]

print(dp[i][1] + dp[i][2] + dp[i][3])
