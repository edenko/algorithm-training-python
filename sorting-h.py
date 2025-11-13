# citations = [5, 6, 7, 8]
# citations = [3, 0, 6, 1, 5]

def solution(citations):
    citations.sort(reverse=True)
    h = 0

    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

print(solution([5, 6, 7, 8]))