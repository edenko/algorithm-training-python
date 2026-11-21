# 📌 정수 삼각형 (BOJ 1932 유형)
# 아래처럼 정수로 이루어진 삼각형이 주어진다.
#    7
#   3 8
#  8 1 0
# 맨 위에서 시작해서
# 아래로 내려가며 인접한 수만 선택할 수 있다.

# 👉 합이 최대가 되는 경로의 합을 구하라.

triangle = [[7], [3, 8], [8, 1, 0]]
n = len(triangle)

dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]

for y in range(1, n):
    for x in range(y + 1):
        if x == 0:
            dp[y][x] = dp[y - 1][x] + triangle[y][x]
        elif x == y:
            dp[y][x] = dp[y - 1][x - 1] + triangle[y][x]
        else:
            dp[y][x] = max(dp[y - 1][x - 1], dp[y - 1][x]) + triangle[y][x]

print(max(dp[n - 1]))
