# 백준 1874 스택 수열

# 1부터 N까지의 정수를 스택에 차례대로 넣을 수 있어.
# 단, 반드시 1 → 2 → 3 → ... → N 순서로만 push할 수 있어.
# 스택에서 pop한 숫자들을 나열해 주어진 목표 수열을 만들어야 해.
# 가능하면 사용한 명령어를 출력하고, 불가능하면 NO를 출력해.
# - + : 스택에 숫자 push
# - - : 스택에서 숫자 pop

# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1

# +
# +
# +
# +
# -
# -
# +
# +
# -
# +
# +
# -
# -
# -
# -
# -

# 5
# 1
# 2
# 5
# 3
# 4

# NO

n = int(input())
stack = []
answer = []

cnt = 1
possible = True

for _ in range(n):
  target = int(input())

  print(cnt, target)

  while cnt <= target:
    stack.append(cnt)
    answer.append('+')
    cnt += 1

  if not stack or stack[-1] != target:
    possible = False
    break
      
  stack.pop()
  answer.append('-')

if possible:
  for n in answer:
    print(n)
else:
  print('NO')
  