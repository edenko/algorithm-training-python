# 조이스틱

name = "JAZ"

count = 0
for char in name:
    count += min(ord(char) - 65, 91 - ord(char))
    
move = len(name) - 1
for i in range(len(name)):
    next = i + 1
    while (next < len(name) and name[next] == 'A'):
        next += 1
    move = min(move, i + len(name) - next + min(i, len(name) - next))

print(count + move)
