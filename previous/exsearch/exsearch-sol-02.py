# 완전탐색 - 모의고사

# 1. 찍는 방식을 정의
# 2. 반복문으로 정답이면 cnt += 1
# 3. 가장 높은 cnt를 리턴, 같으면 오름차순으로 

answers = [1,2,3,4,5,1]
# answers = [1,3,2,4,2]

n1 = [1, 2, 3, 4, 5]
n2 = [2, 1, 2, 3, 2, 4, 2, 5]
n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
c1 = c2 = c3 = 0

for i in range(len(answers)):
    if n1[i % len(n1)] == answers[i]:
        c1 += 1
    if n2[i % len(n2)] == answers[i]:
        c2 += 1
    if n3[i % len(n3)] == answers[i]:
        c3 += 1

rank = max(c1, c2, c3)
scores = [(1, c1), (2, c2), (3, c3)]
answer = sorted(num for num, score in scores if score == rank)

print(answer)