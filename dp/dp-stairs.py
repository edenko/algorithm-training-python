# DP 트레이닝 문제 1 - 계단 오르기

# 5단계
# 1. dp[i] 의미 정하기 : i번째 계단에 오를 경우의 수
# 2. 기본값
# 3. 점화식
# 4. 반복 구조
# 5. 최종 답

n = 5

dp = [float('inf')] * (n + 1)
dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[5])
