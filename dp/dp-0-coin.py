# DP - 동전 교환 (비배수 단위)
# dp[i] = i원을 만드는 최소 동전 개수

# 5단계
# 1. dp[i] 의미 정하기 - “i원을 만드는 최소 동전 수”
# 2. 기본값 - dp[0] = 0 (0원은 동전 0개로 가능)
# 3. 점화식	- dp[i] = min(dp[i], dp[i - coin] + 1)
# 4. 반복 구조 - “모든 동전에 대해 가능한 금액 갱신”
# 5. 최종 답 - dp[k] 출력

coins = [1, 3, 4]
k = 6

dp = [float('inf')] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) # 2
