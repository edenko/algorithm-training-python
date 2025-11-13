# 완전탐색 - 피로도
from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]
total = 0

for comb in permutations(dungeons, len(dungeons)):
    temp = k
    count = 0
    for item in comb:
        if (temp >= item[0]): 
            temp -= item[1]
            if temp >= 0:
                count += 1
            else:
                continue
    
    total = max(total, count)

print(total)
