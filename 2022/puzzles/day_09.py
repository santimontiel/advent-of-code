import math

# Read puzzle.
with open("../data/day_09_test.txt", "r") as file:
    puzzle = list(map(lambda x: x.rstrip().split(" "), file.readlines()))
    puzzle = list(map(lambda x: [x[0], int(x[1])], puzzle))

# Part 1.
def move_head(d, xh, yh):
    if d == "R":
        xh += 1
    if d == "L":
        xh -= 1
    if d == "U":
        yh += 1
    if d == "D":
        yh -= 1
    return xh, yh

def move_tail(d, xt, yt, xh, yh):
    dx = dy = 0
    distance = math.sqrt((xh-xt)**2 + (yh-yt)**2)
    if distance >= 1.5:
        dx = math.fabs(xh - xt)
        dy = math.fabs(yh - yt)
        if d == "R":
            xt += dx - 1
            yt = yh
        if d == "L":
            xt -= dx - 1
            yt = yh
        if d == "U":
            xt = xh
            yt += dy - 1
        if d == "D":
            xt = xh
            yt -= dy - 1
    return xt, yt

visited = set()
xh = yh = xt = yt = 0
for line in puzzle:
    direction, t = line[0], line[1]
    for _ in range(t):
        xh, yh = move_head(direction, xh, yh)
        xt, yt = move_tail(direction, xt, yt, xh, yh)
        visited.add((xt, yt))
print("PRIMERA PARTE:", len(visited), "\n")

# Part 2.
# t_prev = 0
# positions = [[0,0] for _ in range(10)]
# directions = [puzzle[0][0] for _ in range(10)]
# print("****** INIT")
# print(positions)
# print(directions)
# for line in puzzle:
#     direction, t = line[0], line[1]
#     print("******", direction, t)
#     for x in range(t):
#         for i in range(9):
#             positions[i][0], positions[i][1] = move_head(directions[i], positions[i][0], positions[i][1])
#             positions[i][0], positions[i][1] = move_tail(directions[i], positions[i][0], positions[i][1], positions[i-1][0], positions[i-1][1])
#             if i == 9:
#                 visited.add((positions[i+1][0], positions[i+1][1]))
#         print(positions)

#     print(directions)
#     t_prev = t
# print(len(visited))
