# Read puzzle.
with open("../data/day_01.txt", "r") as file:
    content = list(map(lambda x: x.rstrip(), file.readlines()))
print(content)

# Part 1.
elves, this_elf = [], []
for line in content:
    if len(line) != 0:
        this_elf.append(int(line))
    else:
        elves.append(sum(this_elf))
        this_elf = []
print(max(elves))

# Part 2.
sorted_elves = sorted(elves, reverse=True)
print(sum(sorted_elves[:3]))

