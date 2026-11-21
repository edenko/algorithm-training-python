# 공유기 설치 (거리 파라메트릭)

# N개의 집이 일직선상에 있다.
# 각 집의 좌표가 주어질 때,
# 공유기 C개를 설치하려 한다.

# 👉 공유기 사이의 최소 거리를 최대로 하라.

def solution(houses, c):
    houses.sort()
    l, r = 1, houses[len(houses) - 1] - houses[0]
    answer = 0

    def check(mid):
        cnt = 1
        last = houses[0]

        for x in houses[1:]:
            if x - last >= mid:
                cnt += 1
                last = x
        return cnt >= c

    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            l = mid + 1 # 더 늘려도 된다 
        else:
            r = mid - 1
    
    return answer

sol = solution(
    houses = [1, 2, 8, 4, 9],
    C = 3
)
print(sol) # 3