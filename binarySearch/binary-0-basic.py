# 이분탐색이란?
# 정답이 될 수 있는 범위를 반씩 줄여가며 찾는 방법
# 시간복잡도: O(log N)
# 조건: 정렬된 배열 또는 정답이 단조성을 가질 것

# 아래 문장 보이면 반사적으로 이분탐색이다.
# “최대값을 구하라”
# “최소값을 구하라”
# “~할 수 있는 최대 ○○”
# “~를 만족하는 최소 ○○”
# “시간 제한 / 거리 / 용량 / 길이”
# + 
# “최대 / 최소”
# “가능한가?”
# “~시간 안에”
# “~거리로”
# “상한선”

# 📌 문제 1

# 정렬된 정수 배열 arr에서
# 정수 target이 존재하면 인덱스, 없으면 -1을 반환하라.

def solution(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            r = mid - 1

    return -1

sol = solution(
    arr = [1, 3, 5, 7, 9],
    target = 7
)
print(sol) # 3
