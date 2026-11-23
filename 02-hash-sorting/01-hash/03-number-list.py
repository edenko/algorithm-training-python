# 프로그래머스 - 전화번호 목록

# 전화번호가 담긴 배열 phone_book이 주어졌을 때, 
# 어떤 번호가 다른 번호의 **접두어(prefix)**인 경우가 있으면 False, 없으면 True를 반환해.

# 접두어란 문자열의 맨 앞부터 연속된 부분을 의미해.

# phone_book = ["119", "97674223", "1195524421"]

# False

# phone_book = ["123", "456", "789"]

# True

# phone_book = ["12", "123", "1235", "567", "88"]

# False

## 1 set
def solution(phone_book):
    nums = set(phone_book)

    for p in phone_book:
        for i in range(1, len(p)):
            if p[:i] in nums:
                return False

    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

## 2 정렬