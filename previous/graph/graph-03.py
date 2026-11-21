from collections import deque

def solution(arrows):
    d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    visited_node = set()
    visited_edge = set()

    x, y = 0, 0
    visited_node.add((x, y))
    rooms = 0

    for arrow in arrows:
        for _ in range(2):
            nx = x + d[arrow][0]
            ny = y + d[arrow][1]

            edge = ((x, y), (nx, ny))
            reverse_edge = ((nx, ny), (x, y))

            if (nx, ny) in visited_node and edge not in visited_edge:
                rooms += 1
            
            visited_node.add((nx, ny))
            visited_edge.add(edge)
            visited_edge.add(reverse_edge)

            x, y = nx, ny
    
    return rooms

sol = solution(
    arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
)

print(sol) # 3
