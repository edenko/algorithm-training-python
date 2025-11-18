# 그리디 - 구명보트

# people = [150, 120, 80, 80, 70, 40]
people = [70, 80, 50]
limit = 100

people.sort()
left, right = 0, len(people) - 1
count = 0

while left <= right:
    if (people[left] + people[right] <= limit):
        left += 1
    right -= 1
    count += 1

print(count)