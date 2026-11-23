# 상품 코드 정렬하기

# 상품 코드가 문자열 배열로 주어져.

# 다음 기준으로 정렬하는 solution(codes)를 작성해.
# 1. 첫 번째 영문자 오름차순 (A → B)
# 2. 영문자가 같으면 뒤의 숫자 오름차순
# 3. 숫자는 자릿수가 달라도 실제 정수 크기로 비교

# 조건
# - sorted()와 lambda 사용
# - 각 코드는 영문 대문자 한 글자 + 양의 정수로 구성
# - 이중 반복문으로 직접 정렬하지 않기
# - A10과 A2를 문자열 그대로 비교하면 안 됨

# codes = [
#   "A12", "B3", "A2", "B12",
#   "A10", "B1", "A1", "B2"
# ]

# ['A1', 'A2', 'A10', 'A12', 'B1', 'B2', 'B3', 'B12']

def solution(codes):
  # return sorted(codes, key=lambda x: (x[0], int(x[1:])))
  return sorted(codes, key=lambda x: (x[:1], int(x[1:])))