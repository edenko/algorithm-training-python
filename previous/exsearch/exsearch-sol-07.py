# 완전탐색 - 카펫

# 1. 노란색 = (w-2) * (h-2)
# 2. w*h = b + y
# 3. w >= h
brown = 10
yellow = 2
total = brown + yellow

for h in range(1, int(total ** 0.5) + 1):
    if total % h:
        continue
    w = total // h
    if (w - 2) * (h - 2) == yellow:
        print([w, h])
