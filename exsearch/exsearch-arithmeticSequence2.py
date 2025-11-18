# 완전탐색 - 한수 : 자릿수 상관 없음

n = int(input())

count = 0
for i in range(1, n + 1):
    digits = list(map(int, str(i)))
    if len(digits) <= 2:
        count += 1
    else:
        diff = [digits[j] - digits[j + 1] for j in range(len(digits) - 1)]
        if len(set(diff)) == 1:
            count += 1

print(count)
