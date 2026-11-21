# 완전탐색 - 분해합
n = int(input())

result = 0
for i in range(1, n + 1):
    digits = list(map(int, str(i)))
    if (i + sum(digits)) == n:
        result = i
        break

print(result)