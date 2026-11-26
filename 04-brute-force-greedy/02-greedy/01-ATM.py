# 백준 11399 ATM

# ATM이 1대밖에 없다. 지금 이 ATM앞에 N명의 사람들이 줄을 서있다. 
# 사람은 1번부터 N번까지 번호가 매겨져 있으며, 
# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

# 5
# 3 1 4 3 2

# 32

n = int(input())
lines = sorted(list(map(int, input().split())))
total = 0
answer = 0

for i in range(n):
  total += lines[i]
  answer += total

print(answer)
