# 백준 9012 괄호

# 괄호로 이루어진 문자열이 주어졌을 때, 올바른 괄호 문자열(VPS)인지 판단하는 프로그램을 작성해 봐.
# 올바른 괄호 문자열이란 모든 여는 괄호 (가 적절한 닫는 괄호 )와 짝을 이루는 문자열이야.

# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(

# NO
# NO
# YES
# NO
# YES
# NO

n = int(input())

for i in range(n):
  stack = []
  array = input().strip()

  not_matched = False
  for a in array:
    if a == '(':
      stack.append('(')
    elif a == ')':
      if stack:
        stack.pop()
      else:
        not_matched = True
        break

  if stack or not_matched:
    print('NO')
  else:
    print('YES')
