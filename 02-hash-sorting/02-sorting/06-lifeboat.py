# 프로그래머스 - 구명보트

# 무인도에 갇힌 사람들을 구명보트로 구조해야 해.

# 구명보트에는 다음 조건이 있어.
# - 최대 2명까지 탈 수 있어.
# - 탑승한 사람들의 몸무게 합은 limit 이하여야 해.
# - 모든 사람을 구조해야 해.
# - 사용하는 구명보트 수를 최소화해야 해.

# people = [70, 50, 80, 50]
# limit = 100

# 정답: 3

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    a, b = 0, len(people) - 1
    
    while a <= b:
        if a < b and people[a] + people[b] <= limit:
            b -= 1
            
        a += 1
        answer += 1
    
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
