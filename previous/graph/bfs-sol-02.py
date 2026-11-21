# 타겟 넘버 (Programmers)

# 정수 배열 numbers가 주어진다.
# 각 숫자 앞에 + 또는 -를 붙여서
# 모든 숫자를 한 번씩 사용해 target 값을 만들려고 한다.

# 👉 target을 만들 수 있는 경우의 수를 구하라.

# numbers = [1, 1, 1, 1, 1]
# target = 3
## 5

def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer

        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return
        
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])


    dfs(0, 0)
    return answer
    
sol = solution([1, 1, 1, 1, 1], 3)
print(sol) # 5