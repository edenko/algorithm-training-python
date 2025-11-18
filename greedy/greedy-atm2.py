# 그리디 - atm 응용 : 줄 서는 순서에 따른 총 대기시간 비교
# 가장 효율적인 시간 총합, 가장 비효율적인 시간 총합

n = 5
times = [3, 1, 4, 3, 2]

total = [0, 0]
acc = [0, 0]

time1 = sorted(times)
time2 = sorted(times, reverse=True)

for idx in range(len(times)):
    total[0] += time1[idx]
    total[1] += time2[idx]
    acc[0] += total[0]
    acc[1] += total[1]

print(acc)
