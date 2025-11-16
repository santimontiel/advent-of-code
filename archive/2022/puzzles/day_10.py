# Read puzzle.
with open("../data/day_10.txt", "r") as file:
    puzzle = list(map(lambda x: x.rstrip(), file.readlines()))

# Part 1.
cycles = [1]
for line in puzzle:
    if line.startswith("noop"):
        cycles.append(cycles[-1])
    if line.startswith("addx"):
        cycles.append(cycles[-1])
        cycles.append(cycles[-1] + int(line.split(" ")[1]))

signal = sum(cycles[i-1]*i for i in [20, 60, 100, 140, 180, 220])
print(signal)

# Part 2.
mat = []
for i in range(0, 6):
    this_row = []
    for j in range(0, 40):
        k = 40*i + j
        if j-1 <= cycles[k] <= j+1: 
            this_row.append("#")
        else:
            this_row.append(" ")
    mat.append(''.join(x for x in this_row))

from pprint import pprint
pprint(mat)