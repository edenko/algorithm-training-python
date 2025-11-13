from collections import Counter

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

cnt = Counter(map(lambda x: x[1], clothes)) 
result = 1

for key, value in cnt.items(): 
    result *= (value + 1) # 안 입는 경우의 수 추가

print(result - 1) # 아무 것도 안 입는 경우는 제외
