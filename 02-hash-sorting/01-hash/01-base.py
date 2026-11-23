# 1. 숫자 등장 횟수 세기

# 각 숫자가 몇 번 등장하는지 딕셔너리에 저장해.
# 가장 많이 등장한 숫자를 출력해.
# Counter는 사용하지 말고, dict와 get()으로 구현해.

nums = [3, 1, 2, 3, 2, 3, 4, 1, 4, 4, 4, 4, 4]

dic = {}
for n in nums:
  dic[n] = dic.get(n, 0) + 1

print(max(dic, key=lambda x: dic[x]))
print(max(dic, key=dic.get))



# 2. 두 수의 합 (Two Sum)

# 정수 배열 nums와 정수 target이 주어졌어.
# 배열에서 서로 다른 위치의 숫자 두 개를 더해 target이 되는 인덱스를 찾아 반환해.
# 이중 반복문 O(N²) 대신 **딕셔너리로 평균 O(N)**

# nums = [2, 7, 11, 15]
# target = 9

# [0, 1]

def solution(nums, target):
  seen = {}

  idx = 0
  for n in nums:
    need = target - n

    if need in seen:
      return [seen[need], idx]

    seen[n] = idx
    idx += 1

print(solution([2, 7, 11, 15], 9))



# 3. 애너그램 그룹 만들기

# 문자열 배열이 주어졌을 때, 문자 구성은 같고 순서만 다른 단어들을 같은 그룹으로 묶어 반환해.
# 애너그램(Anagram)이란 문자 종류와 각 문자의 등장 횟수가 같은 문자열을 의미해.

# 조건
# - 딕셔너리를 사용해서 구현해.
# - 모든 단어는 영어 소문자로 구성되어 있어.
# - 같은 단어가 여러 번 등장하면 등장 횟수만큼 포함해.
# - 이중 반복문으로 모든 단어를 서로 비교하는 방식은 피해야 해.

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]

def solution(words):
  dic = {}

  for w in words:
    word = ''.join(sorted(w))

    temp = dic.get(word, [])
    temp.append(w)
    dic[word] = temp

  return list(dic.values())

print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))



# 가장 긴 연속 숫자 수열

# 정수 배열 nums가 주어졌을 때, 
# 숫자의 순서와 관계없이 연속된 정수로 이루어진 가장 긴 수열의 길이를 구해 봐.

# - 입력 숫자의 순서는 상관없어.
# - 중복된 숫자는 한 번만 취급해.
# - 빈 배열이라면 0을 반환해.
# - sorted()를 사용하지 말고, set을 사용해 **평균 O(N)**으로 해결해 봐.

# nums = [100, 4, 200, 1, 3, 2]

# 4

def solution(nums):
  numbers = set(nums)
  longest = 0

  for n in numbers:
    if n - 1 not in numbers: # 시작점이 될 수 있는 n
      current = n
      length = 1

      while current + 1 in numbers:
        current += 1
        length += 1

      longest = max(length, longest)
  return longest

print(solution([100, 4, 200, 1, 3, 2]))
