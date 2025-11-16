from collections import namedtuple

Number = namedtuple("Number", ["value", "index"])

with open("day_01_input.txt") as f:
    data = f.read().splitlines()

right_numbers, left_numbers = [], []
for i, d in enumerate(data):
    l, r = d.split("   ")
    left_numbers.append(Number(int(l), i))
    right_numbers.append(Number(int(r), i))

left_numbers.sort(key=lambda x: x.value)
right_numbers.sort(key=lambda x: x.value)

# Part 1.
distance = 0
for left, right in zip(left_numbers, right_numbers):
    distance += abs(left.value - right.value)
print(distance)


# Part 2. Although sorting is not needed.
similarity = 0
for left in left_numbers:
    count = sum(1 for right in right_numbers if right.value == left.value)
    similarity += left.value * count
print(similarity)

