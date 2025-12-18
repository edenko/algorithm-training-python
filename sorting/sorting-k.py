array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
res = []

for cond in commands:
    temp = array[cond[0] - 1: cond[1]]
    temp.sort()
    res.append(temp[cond[2] - 1])

print(res)