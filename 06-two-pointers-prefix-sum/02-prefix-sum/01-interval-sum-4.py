# 백준 11659 — 구간 합 구하기 4

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

# 12
# 9
# 1

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0] * (n + 1)
answer = []

for i in range(1, n + 1):
  prefix[i] = prefix[i - 1] + nums[i - 1]

for i in range(m):
  a, b = map(int, input().split())
  answer.append(prefix[b] - prefix[a - 1])

for a in answer:
  print(a)
