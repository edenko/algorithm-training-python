arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

dp = [0] * len(arr)
dp[0] = 0

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))

current = arr[0]
answer = arr[0]

for i in range(1, len(arr)):
    current = max(arr[i], current + arr[i])
    answer = max(answer, current)

print(answer)