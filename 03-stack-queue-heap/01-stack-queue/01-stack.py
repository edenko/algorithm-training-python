# 백준 10828 스택

# 정수를 저장하는 스택을 구현하고, 입력으로 주어지는 명령을 처리하는 프로그램을 작성해 봐.
# 지원해야 하는 명령은 다음과 같아.

# 명령	처리
# push X	X를 스택에 추가
# pop	가장 위 정수를 제거하고 출력, 비어 있으면 -1
# size	스택에 들어 있는 정수 개수 출력
# empty	비어 있으면 1, 아니면 0 출력
# top	맨 위 정수 출력, 비어 있으면 -1

# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top

# 2
# 2
# 0
# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3

n = int(input())
stack = []

for i in range(n):
  string = input()

  if string == 'size':
    print(len(stack))
  elif string == 'empty':
    print(0 if stack else 1)
  elif string == 'top':
    print(stack[-1] if stack else -1)
  elif string == 'pop':
      print(stack.pop() if stack else -1)
  elif string.startswith('push'):
    txt, number = string.split()
    stack.append(int(number))
