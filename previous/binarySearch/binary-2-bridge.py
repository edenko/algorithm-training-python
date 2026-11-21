# 징검다리 이분탐색

# 출발지점부터 도착지점까지의 거리 distance, 
# 바위들이 있는 위치를 담은 배열 rocks, 
# 제거할 바위의 수 n이 매개변수로 주어질 때, 

# 바위를 n개 제거한 뒤 
# 각 지점 사이의 거리의 최솟값 중에 
# 가장 큰 값을 return

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    l, r = 1, distance

    def check(mid):
        remove = 0
        prev = 0

        for rock in rocks:
            if rock - prev < mid:
                remove += 1
            else:
                prev = rock
        
        if distance - prev < mid:
            remove += 1

        return remove <= n
    
    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
        
    return answer

sol = solution(
    distance = 25,
    rocks = [2, 14, 11, 21, 17],
    n = 2
)
print(sol)
