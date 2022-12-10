import math

# Read puzzle.
with open("../data/day_09_test.txt", "r") as file:
    puzzle = list(map(lambda x: x.rstrip().split(" "), file.readlines()))
    puzzle = list(map(lambda x: [x[0], int(x[1])], puzzle))

# Part 1.
def move_head(d, xh, yh):
    if d == "R": xh += 1
    if d == "L": xh -= 1
    if d == "U": yh += 1
    if d == "D": yh -= 1
    return xh, yh

def move_tail(xt, yt, xh, yh):
    dx = xh-xt
    dy = yh-yt
    if dx**2 + dy**2 > 2:
        if dx != 0:
            xt += 1 if dx > 0 else -1
        if dy != 0:
            yt += 1 if dy > 0 else -1
    return xt, yt

xh = yh = xt = yt = 0
vis = {(0,0)}
for line in puzzle:
    for n in range(int(line[1])):
        xh, yh = move_head(line[0], xh, yh)
        xt, yt = move_tail(xt, yt, xh, yh)
        vis.add((xt, yt))
print(len(vis))

# Part 2.
poses = [[0,0] for _ in range(10)]
vis = set()
for line in puzzle:
    for n in range(line[1]):
        poses[0][0], poses[0][1] = move_head(line[0], poses[0][0], poses[0][1])
        for i in range(1, 10):
            poses[i][0], poses[i][1] = move_tail(poses[i][0], poses[i][1], poses[i-1][0], poses[i-1][1])
        vis.add((poses[-1][0], poses[-1][1]))
print(len(vis))
