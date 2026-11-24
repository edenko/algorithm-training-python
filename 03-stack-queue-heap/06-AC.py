# 백준 5430 AC

# 정수 배열에 두 가지 명령을 수행하는 프로그램을 작성해야 해.

# 명령	의미
# R	배열에 있는 숫자의 순서를 뒤집는다
# D	배열의 첫 번째 숫자를 버린다

# 단, 배열이 비어 있을 때 D를 실행하면 error를 출력해야 해.
# 명령어들이 문자열로 주어지고, 모든 명령을 실행한 뒤 최종 배열을 출력해야 해.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
# 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []

# [2,1]
# error
# [1,2,3,5,8]
# error

from collections import deque

t = int(input())

for _ in range(t):
  p = input().strip()
  n = int(input())
  array = input().strip()[1:-1].split(',')
  cnt_R = 0
  is_error = False

  q = deque() if n == 0 else deque(array)

  for pp in p:

    if not q and pp == 'D':
      is_error = True
      break

    if pp == 'R':
      cnt_R += 1
    elif pp == 'D':
      if cnt_R % 2 == 0:
        q.popleft()
      else:
        q.pop()

  if is_error:
    print('error')
    continue

  if cnt_R % 2 != 0:
    q.reverse()

  print('[' + ','.join(map(str, q)) + ']')
  