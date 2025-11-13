# 완전탐색 - 소수 찾기
from itertools import permutations

numbers = "011"

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True 

nums = set()
for r in range(1, len(numbers) + 1):
    for p in permutations(numbers, r):
        nums.add(int(''.join(p)))

count = 0
for num in nums:
    if is_prime(num):
        count += 1

print(count)