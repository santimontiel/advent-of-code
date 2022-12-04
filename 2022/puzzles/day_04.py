# Read puzzle.
with open("../data/day_04.txt", "r") as file:
    content = list(map(lambda x: x.rstrip().
                                   replace("-",",").
                                   split(","),
                file.readlines()))

counter = 0
for z in content:
    a, b, c, d = int(z[0]), int(z[1]), int(z[2]), int(z[3])
    if (a <= c and b >= d) or (a >= c and b <= d):
        counter += 1
print(counter)

counter = 0
for z in content:
    a, b, c, d = int(z[0]), int(z[1]), int(z[2]), int(z[3])
    if (b >= c and a <= d):
        counter += 1
print(counter)