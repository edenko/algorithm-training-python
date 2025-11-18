# 완전탐색 - 셀프넘버 : 분해합 반대개념

def func(n):
    return n + sum(list(map(int, str(n))))

result = set(range(1, 10001))
gener = set()

for i in range(1, 10001):
    gener.add(func(i))

print(sorted(list(map(int, result - gener))))