# Read puzzle.
with open("../data/day_02.txt", "r") as file:
    content = list(map(lambda x: x.rstrip().split(" "), file.readlines()))

# A: Rock, B: Paper, C: Scissors -> Opponent
# X: Rock, Y: Paper, Z: Scissors -> Your Play

# Part 1.
def play_rps(opponent, play):
    if play == opponent:
        return 3
    if play == "s" and opponent in "p":
        return 6
    if play == "p" and opponent in "r":
        return 6
    if play == "r" and opponent in "s":
        return 6
    return 0

mapping = {
    "X": "r", "Y": "p", "Z": "s",
    "A": "r", "B": "p", "C": "s",
}
score_map = {
    "X": 1, "Y": 2, "Z": 3
}

score = list(map(lambda x: score_map[x[1]], content))
remap = list(map(lambda x: play_rps(mapping[x[0]], mapping[x[1]]), content))
print(sum(score + remap))

# Part 2.
# X: Lose, Y: Draw, Z: Win
scores = [1, 2, 3]

remap_2 = {
    "A": 0, "B": 1, "C": 2
}
remap_3 = {
    "X": -1, "Y": 0, "Z": 1
}
remap_4 = {
    "X": 0, "Y": 3, "Z": 6,
}
scores_2 = list(map(lambda x: scores[(remap_2[x[0]] + remap_3[x[1]]) % 3] + remap_4[x[1]], content))
print(sum(scores_2))
