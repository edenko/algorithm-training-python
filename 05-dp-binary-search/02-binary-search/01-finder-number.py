# 백준 1920 — 수 찾기

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 1
# 1
# 0
# 0
# 1

n = int(input())
target = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

target.sort()

for ar in array:
  left = 0
  right = n - 1
  find = False

  while left <= right:
    mid = (left + right) // 2

    if target[mid] == ar:
      find = True
      break
    elif target[mid] < ar:
      left = mid + 1
    else:
      right = mid - 1

  print(1 if find else 0)
  