from copy import deepcopy

# Read puzzle.
with open("../data/day_11.txt", "r") as file:
    puzzle = list(map(lambda x: x.rstrip(), file.readlines()))

monkey = monkeys = []
for line in puzzle:
    if line.startswith("Monkey"):
        if len(monkey) != 0: monkeys.append(monkey)
        monkey = []
    if "Starting items" in line:
        monkey.append(list(map(int, line[18:].replace(",", "").split(" "))))
    if "Operation" in line:
        splitted = line[20:].split(" ")
        op1 = "add" if splitted[1] == "+" else "mult"
        op2 = splitted[2] if splitted[2] == "old" else int(splitted[2])
        monkey.append([op1, op2])
    if "Test" in line:
        monkey.append(int(line.split(" ")[-1]))
    if "If true" in line:
        monkey.append(int(line[-1]))
    if "If false" in line:
        monkey.append(int(line[-1]))
monkeys.append(monkey)
monkeys_2 = deepcopy(monkeys)

# Part 1.
rounds = 20
cnt = [0 for x in range(len(monkeys))]
for i in range(rounds):
    for k, monkey in enumerate(monkeys):          # Iterate through items.
        # print("\n*", "NEW MONKEY")
        for j in range(len(monkey[0])):
            cnt[k] += 1
            this_item = monkey[0][0]    # Take this item.
            monkey[0] = monkey[0][1:]   # Eliminate from this bag.
            if monkey[1][0] == "add":
                this_item = this_item + monkey[1][1]
            elif monkey[1][0] == "mult" and monkey[1][1] == "old":
                this_item = this_item * this_item
            elif monkey[1][0] == "mult":
                this_item = this_item * monkey[1][1]
            if int(this_item / 3) % monkey[2] == 0:
                monkeys[monkey[3]][0].append(int(this_item / 3))
            else:
                monkeys[monkey[4]][0].append(int(this_item / 3))

prod = lambda x: x[0] * x[1]
print(prod(sorted(cnt, reverse=True)[:2]))

# Part 2.
mod = 1
for monkey in monkeys_2:
    mod *= monkey[2]

rounds = 10000
cnt = [0 for x in range(len(monkeys_2))]
for i in range(rounds):
    for k, monkey in enumerate(monkeys_2):          # Iterate through items.
        # print("\n*", "NEW MONKEY")
        for j in range(len(monkey[0])):
            cnt[k] += 1
            this_item = monkey[0][0]    # Take this item.
            monkey[0] = monkey[0][1:]   # Eliminate from this bag.
            if monkey[1][0] == "add":
                this_item = this_item + monkey[1][1]
            elif monkey[1][0] == "mult" and monkey[1][1] == "old":
                this_item = this_item * this_item
            elif monkey[1][0] == "mult":
                this_item = this_item * monkey[1][1]
            this_item = this_item % mod
            if this_item % monkey[2] == 0:
                monkeys_2[monkey[3]][0].append(this_item)
            else:
                monkeys_2[monkey[4]][0].append(this_item)
print(prod(sorted(cnt, reverse=True)[:2]))
  