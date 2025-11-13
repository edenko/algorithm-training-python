i = int(input())
lists = list(map(int, input().split()))
lists.sort()

total = 0
acc = 0
for item in lists[:i]:
    total += item
    acc += total

print(acc)
