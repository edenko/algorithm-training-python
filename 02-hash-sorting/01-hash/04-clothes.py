# 프로그래머스 - 의상

# 서로 다른 옷들의 이름과 종류가 clothes 배열로 주어져.

# 옷을 조합해서 입을 때 다음 조건을 만족해야 해.
# - 같은 종류의 옷은 최대 한 개만 입을 수 있어.
# - 서로 다른 종류의 옷은 함께 입을 수 있어.
# - 적어도 한 개의 옷은 반드시 입어야 해.
# - 서로 다른 옷 조합의 총개수를 반환해.

# clothes = [
#   ["yellow_hat", "headgear"], 
#   ["blue_sunglasses", "eyewear"], 
#   ["green_turban", "headgear"]
# ]

# 출력: 5

# clothes = [
#   ["crow_mask", "face"],
#   ["blue_sunglasses", "face"],
#   ["smoky_makeup", "face"]
# ]

# 출력: 3

def solution(clothes):
    answer = 1
    dic = {}
    
    for k, c in clothes:
        dic[c] = dic.get(c, 0) + 1

    for k, v in dic.items():
        answer *= v + 1
    
    return answer - 1