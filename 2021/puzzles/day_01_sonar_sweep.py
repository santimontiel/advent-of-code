# Read puzzle.
with open("../data/day_01.txt", "r") as file:
    content = list(map(lambda x: int(x), file.readlines()))

# Part 1.
pairs = list(zip(content[1:], content[:-1]))
increases = sum(list(map(lambda x: x[0] > x[1], pairs)))
print(f"Solution for part 1 is: {increases}")

# Part 2.
pairs = list(zip(content[3:], content[:-3]))
increases =  sum(list(map(lambda x: x[0] > x[1], pairs)))
print(f"Solution for part 2 is: {increases}")

