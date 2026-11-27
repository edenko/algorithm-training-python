# 백준 21921 — 블로그

# 찬솔이는 블로그를 시작한 지 벌써 N일이 지났다.
# 요즘 바빠서 관리를 못 했다가 방문 기록을 봤더니 벌써 누적 방문 수가 6만을 넘었다.

# 찬솔이는 X일 동안 가장 많이 들어온 방문자 수와 그 기간들을 알고 싶다.
# 찬솔이를 대신해서 X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

# 첫째 줄에 블로그를 시작하고 지난 일수 N와 X가 공백으로 구분되어 주어진다.
# 둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.

# 첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다. 
# 만약 최대 방문자 수가 0명이라면 SAD를 출력한다.
# 만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.

# 5 2
# 1 4 2 5 1

# 7
# 1

# 7 5
# 1 1 1 1 1 5 1

# 9
# 2

# 5 3
# 0 0 0 0 0

# SAD

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
