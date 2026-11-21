# 구현 / 시뮬레이션이란?

# 문제에서 시키는 대로 그대로 구현하는 유형

# 알고리즘 난이도는 낮아 보이지만
# 👉 조건 누락 / 좌표 실수 / 순서 실수 때문에 많이 틀림

# 💡 “아이디어는 쉬운데, 코드가 길고 귀찮은 문제”

# 구현 문제에서 반드시 체크해야 할 것들
# - 입력 크기 (N, M 최대값)
# - 좌표 기준 (x, y / row, col / 0-index or 1-index)
# - 순서 중요 여부 (동시에? 순차적으로?)
# - 상태가 바뀌는지 (원본 보존 필요?)

# 문제 1️⃣ (워밍업)

# N×N 격자가 있다.
# 시작 위치는 (0, 0)
# 명령 문자열이 주어진다.
# (U, D, L, R)

# 격자 밖으로 나가는 명령은 무시한다.
# 최종 위치를 출력하라.

def solution(n, commands):
    x, y = 0, 0
    move = {
        'D': (0, 1),
        'R': (1, 0),
        'U': (0, -1),
        'L': (-1, 0),
    }

    for cmd in commands:
        dx, dy = move[cmd]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            x = nx
            y = ny

    return (x, y)

sol = solution(
    n = 5,
    commands = "RRRUDD"
)
print(sol) # (3, 2)
