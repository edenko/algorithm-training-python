# 문제 2 (파라메트릭 서치 핵심)
# 📌 문제 설명 (랜선 자르기 유형)

# 길이가 서로 다른 랜선 arr이 N개 있다.
# 이 랜선들을 같은 길이로 잘라서,
# 최소 M개 이상의 랜선을 만들고 싶다.

# 👉 만들 수 있는 랜선 길이의 최댓값을 구하라.

# ✔ 조건
# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 1,000,000
# 랜선 길이는 모두 자연수
# 시간복잡도: O(N log max(arr)) 요구

def solution(arr, target):
    l, r = 1, max(arr)
    answer = 0

    def check(length):
        cnt = 0
        for x in arr: 
            cnt += x // length
        return cnt >= target

    while l <= r:
        mid = (l + r) // 2

        if check(mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1

    return answer

sol = solution(
    arr = [802, 743, 457, 539],
    target = 11
)
print(sol) # 200
