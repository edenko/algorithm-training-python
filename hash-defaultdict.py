from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
res = []

dic = defaultdict(list)
for i in range(len(genres)):
    dic[genres[i]].append((i, plays[i]))

for k, v in dic.items():
    v.sort(key=lambda x: (-x[1], x[0]))

total = { g: sum(p for _, p in s) for g, s in dic.items()}
total = sorted(total.items(), key=lambda x: -x[1])

for i in total: 
    idx = 0
    for j in dic[i[0]]:
        if (idx < 2):
            res.append(j[0])
            idx += 1

print(res)