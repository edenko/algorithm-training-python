# 체육복

n = 5
lost = [1, 3, 4]
reserve = [1, 2, 3]	
lost_s = set(lost) - set(reserve)
reserve_s = set(reserve) - set(lost)

found = 0
for item in lost_s:
    if (item - 1 in reserve_s):
        reserve_s.remove(item - 1)
        found += 1
    elif (item + 1 in reserve_s):
        reserve_s.remove(item + 1)
        found += 1

print(n - len(lost_s) - found)

