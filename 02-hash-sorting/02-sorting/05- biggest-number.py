# 프로그래머스 - 가장 큰 수

# 0 또는 양의 정수가 담긴 배열 numbers가 주어져.
# 숫자들의 순서를 자유롭게 바꾼 뒤, 전부 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 반환해 봐.

# 조건
# - numbers의 길이는 1 이상 100,000 이하
# - 각 원소는 0 이상 1,000 이하
# - 반환값은 정수가 아니라 문자열
# - 모든 숫자가 0일 수도 있음

# numbers = [3, 30, 34, 5, 9]

# 반환값: "9534330"

from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    return 0

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    return '0' if numbers[0] == '0' else ''.join(numbers)
