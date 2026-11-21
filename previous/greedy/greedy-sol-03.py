# 그리디 - 큰 수 만들기

number = "10"
k = 1
stack = []

for num in number:
    print(num)
    while stack and stack[-1] < num and k > 0:
        print(stack)
        stack.pop()
        k -= 1
    stack.append(num)

if k != 0:
    stack.pop()
print(stack)
