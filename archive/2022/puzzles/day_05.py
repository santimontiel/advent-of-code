# Read puzzle.
with open("../data/day_05.txt", "r") as file:
    content = list(map(lambda x: x.rstrip(), file.readlines()))
    raw_towers = list(map(lambda x: x.ljust(35), content[:8]))
    moves = content[10:]

# Parse original towers.
towers = []
for i in range(1, 10):
    tower = ""
    for t in range(0, 8):
        tower += raw_towers[7-t][1 + ((i-1)*4)]
    towers.append(tower.rstrip())
towers_p2 = towers.copy()

# Part 1.
for line in moves:
    splitted = line.split(" ")
    n, src, dst = int(splitted[1]), int(splitted[3]), int(splitted[5])
    for i in range(0, n):
        c = towers[src-1][-1]
        towers[src-1] = towers[src-1][:-1]
        towers[dst-1] += c

ans = ''.join([tower[-1] for tower in towers])
print(ans)

# Part 2.
for line in moves:
    splitted = line.split(" ")
    n, src, dst = int(splitted[1]), int(splitted[3]), int(splitted[5])
    c = towers_p2[src-1][-n:]
    towers_p2[src-1] = towers_p2[src-1][:-n]
    towers_p2[dst-1] += c

ans = ''.join([tower[-1] for tower in towers_p2])
print(ans)