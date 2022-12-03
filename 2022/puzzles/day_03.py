# Read puzzle.
with open("../data/day_03.txt", "r") as file:
    content = list(map(lambda x: x.rstrip(), file.readlines()))

def calculate_prio(char) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26

# Part 1.
prios = []
for string in content:
    half = int(len(string)/2)
    for char in string[:half]:
        if char in string[half:]:
            prio = calculate_prio(char)
            prios.append(prio)
            break
print(sum(prios))

# Part 2.
prios = []
groups = [(x, x + 1, x + 2) for x in range(0, len(content), 3)]
for group in groups:
    f, s, t = content[group[0]], content[group[1]], content[group[2]]
    for char in f:
        if char in s and char in t:
            prios.append(calculate_prio(char))
            break
print(sum(prios))
