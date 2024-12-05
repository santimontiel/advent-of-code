with open("day_05_input.txt", "r") as f:
    data = f.read().splitlines()

rules = list()
sequences = list()

for line in data:
    if len(line) == 5:
        rules.append(line)
    elif line == "":
        continue
    else:
        t = line.split(",")
        t = [int(x) for x in t]
        sequences.append(t)


# Part 1.
count = 0
incorrect = []  # Accumulate for part 2.
for sequence in sequences:
    cond = True
    middle_number = sequence[len(sequence) // 2]
    for i in range(len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if f"{sequence[j]}|{sequence[i]}" in rules:
                cond = False
    if cond:
        count += middle_number
    else:
        incorrect.append(sequence)

print(count)


# Part 2.
def check(sequence, rules):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sequence) - 1):
            for j in range(i + 1, len(sequence)):
                if f"{sequence[j]}|{sequence[i]}" in rules:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                    swapped = True
    return sequence

count = 0
for sequence in incorrect:
    correct = check(sequence, rules)
    middle_number = sequence[len(correct) // 2]
    count += middle_number

print(count)