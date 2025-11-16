from copy import deepcopy

with open("day_02_input.txt") as f:
    data = f.read().splitlines()
    data = [[int(x) for x in line.split()] for line in data]


def is_safe(level_diffs):
    return (
        all(diff > 0 for diff in level_diffs)
        or all(diff < 0 for diff in level_diffs)
    ) and (all(abs(diff) <= 3 for diff in level_diffs))

# Part 1.
safe = 0
for line in data:
    level_diffs = [p2 - p1 for p1, p2 in zip(line, line[1:])]
    safe += is_safe(level_diffs)

print(safe)

# Part 2.
safe = 0
for line in data:
    level_diffs = [p2 - p1 for p1, p2 in zip(line, line[1:])]
    if is_safe(level_diffs):
        safe += 1
    else:
        for i in range(len(line)):
            new_line = line[:i] + line[i+1:]
            new_level_diffs = [p2 - p1 for p1, p2 in zip(new_line, new_line[1:])]
            if is_safe(new_level_diffs):
                safe += 1
                break

print(safe)