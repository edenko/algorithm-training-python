# 카테고리별 인기 상품 선정

# 상품 정보가 (카테고리, 상품명, 판매량) 형태로 주어져.

# 정렬 조건
# 1. 같은 카테고리의 상품들을 묶는다.
# 2. 카테고리별 총판매량이 높은 순서로 카테고리를 정렬한다.
# 3. 각 카테고리 내부에서는 상품 판매량 내림차순으로 정렬한다.
# 4. 판매량이 같으면 상품명 오름차순으로 정렬한다.
# 5. 카테고리별 상위 2개 상품명만 결과에 추가한다.
# 6. 카테고리 총판매량이 같으면 카테고리명 오름차순으로 정렬한다.

# products = [
#   ("food", "apple", 100),
#   ("tech", "mouse", 300),
#   ("food", "banana", 200),
#   ("tech", "keyboard", 300),
#   ("food", "orange", 150),
#   ("book", "novel", 250)
# ]

# ["keyboard", "mouse", "banana", "orange", "novel"]

def solution(products):
    answer = []
    categories = {}
    groups = {}

    for cate, name, sales in products:
      categories[cate] = categories.get(cate, 0) + sales
      temp = groups.get(cate, [])
      temp.append((name, sales))
      groups[cate] = temp

    categories = sorted(categories, key=lambda x: (-categories[x], x))

    for category in categories:
      group = sorted(groups[category], key=lambda x: (-x[1], x[0]))[:2]
      for name, _ in group:
         answer.append(name)
        
    return answer

products = [
  ("food", "apple", 100),
  ("tech", "mouse", 300),
  ("food", "banana", 200),
  ("tech", "keyboard", 300),
  ("food", "orange", 150),
  ("book", "novel", 250)
]
print(solution(products))
