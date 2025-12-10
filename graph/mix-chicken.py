# [문제 18] 치킨 배달 — BOJ 15686
# 브루트포스 + 조합 + 거리 계산의 핵심 문제

# 도시가 N×N 격자이고 각 위치는 다음 중 하나다
# 0 → 빈 칸 / 1 → 집 / 2 → 치킨집
# 도시 치킨집 중에서 M개만 남기고, 나머지는 폐업시켜야 한다.

# 모든 집이 “가장 가까운 치킨집”까지의 거리의 합을 최소화하는 것
# → 이것을 **도시 치킨 거리(city chicken distance)**라고 한다.
# 거리 = |x1-x2| + |y1-y2| (맨해튼 거리)
from itertools import combinations

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for y in range(n):
    for x in range(n):
        if grid[y][x] == 2:
            chicken.append((x, y))
        elif grid[y][x] == 1:
            house.append((x, y))

def calc_distance(combo):
    total = 0
    for hx, hy in house:
        dist = float('inf')
        for cx, cy in combo:
            d = abs(hx - cx) + abs(hy - cy)
            dist = min(dist, d)
        total += dist
    return total

answer = float('inf')

for combo in combinations(chicken, m):
    total = calc_distance(combo)
    answer = min(answer, total)

print(answer) # 5