from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def cal_text(a, b):
        diff = [1 for x, y in zip(a, b) if x != y]
        return diff == 1

    q = deque()
    q.append((begin, 0))
    checked = set()
    checked.add(begin)

    while q:
        word, cnt = q.popleft()

        if word == target:
            return cnt
        
        for w in words:
            if w not in checked and cal_text(word, w):
                checked.add(w)
                q.append((w, cnt + 1))

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))