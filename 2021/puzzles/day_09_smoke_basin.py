# Read puzzle.
with open("../data/day_09_test.txt", "r") as file:
    content = list(map(lambda x: x.rstrip(), file.readlines()))

# Part 1.
tubes = 0
tubes_positions = []
for i, line in enumerate(content):
    for j, char in enumerate(line):
        neighbors = []
        if i != 0:
            neighbors += content[i-1][j]        # Upper neighbor.
        if i != len(content) - 1:
            neighbors += content[i+1][j]        # Bottom neighbor.
        if j != 0:
            neighbors += line[j-1]              # Left neighbor.
        if j != len(line) - 1:
            neighbors += line[j+1]              # Right neighbor.
        lowest = sum(list(map(lambda x: int(char) < int(x), neighbors))) == len(neighbors)
        if lowest:
            tubes += int(char) + 1
            tubes_positions.append((i, j))      # Append seed for part 2.
            
print(tubes)
print(tubes_positions)

# Part 2.
for i, j in tubes_positions:
    neighbors = []
    if i != 0:
        neighbors += content[i-1][j]        # Upper neighbor.
    if i != len(content) - 1:
        neighbors += content[i+1][j]        # Bottom neighbor.
    if j != 0:
        neighbors += line[j-1]              # Left neighbor.
    if j != len(line) - 1:
        neighbors += line[j+1]              # Right neighbor
    
