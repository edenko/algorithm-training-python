# 완전탐색 - 한수 : 세자리

n = int(input())

count = 0
for i in range(1, n + 1):
    if i < 100:
        count += 1
    else:
        digit = list(map(int, str(i)))
        print(digit)
        if digit[0] - digit[1] == digit[1] - digit[2]:
            count += 1
