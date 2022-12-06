# Read puzzle.
with open("../data/day_06.txt", "r") as file:
    x = file.read()

# Part 1.
for i in range(0, len(x[:-3])):
    this_set = {x[i], x[i+1], x[i+2], x[i+3]}
    if (len(this_set) == 4):
        print(i+4, sorted(this_set))
        break
    
# Part 2.
for i in range(0, len(x[:-13])):
    this_set = set()
    for j in range(0,14):
        this_set.add(x[i+j])
    if (len(this_set) == 14):
        print(i+14, sorted(this_set))
        break
    