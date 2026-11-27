n, x = map(int, input().split())
nums = list(map(int, input().split()))

total = 0
answer = 0
count = 1

for i in range(x):
  total += nums[i]

for i in range(x, n):
  total += nums[i] - nums[i - x]

  if total > answer:
    answer = total
    count = 1
  elif total == answer:
    count += 1

if answer == 0:
  print('SAD')
else:
  print(answer)
  print(count)
