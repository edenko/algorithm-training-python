# 백준 2579 계단 오르기

# 계단마다 점수가 주어져 있고, 다음 규칙을 지키면서 맨 위 계단까지 올라가야 해.
# 1. 한 번에 1계단 또는 2계단 올라갈 수 있어.
# 2. 연속된 3개의 계단을 모두 밟으면 안 돼. (시작 지점은 계단으로 세지 않아.)
# 3. 마지막 계단은 반드시 밟아야 해.
# 4. 밟은 계단의 점수 합계를 최대화해야 해.

# 6
# 10
# 20
# 15
# 25
# 10
# 20

# 75

n = int(input())
points = []

for _ in range(n):
  points.append(int(input()))

dp = [0] * (n + 1)

dp[1] = points[0]
if n > 1:
  dp[2] = points[0] + points[1]

  for i in range(3, n + 1):
    a = dp[i - 2] + points[i - 1]
    b = dp[i - 3] + points[i - 2] + points[i - 1]

    dp[i] = max(a, b)
    
print(dp[n])
