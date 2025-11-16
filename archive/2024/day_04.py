with open("day_04_input.txt") as f:
    data = f.read().splitlines()

# Part 1.
PATTERNS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]

count = 0
for j, line in enumerate(data):
    for i, char in enumerate(line):
        if char == "X":
            for p in PATTERNS:
                if 0 <= i + 3 * p[0] < len(line) and 0 <= j + 3 * p[1] < len(data):
                    substr = ""
                    for k in range(4):
                        substr += data[j + k * p[1]][i + k * p[0]]
                    if substr == "XMAS":
                        count += 1

print(count)

# Part 2.
def get_kernel_3x3(i, j, data):
    return [line[i:i+3] for line in data[j:j+3]]

PATTERNS = [
    ["M", "M", "S", "S"],
    ["S", "S", "M", "M"],
    ["M", "S", "M", "S"],
    ["S", "M", "S", "M"],
]

count = 0
for j, line in enumerate(data[:-2]):
    for i, char in enumerate(line[:-2]):
        k = get_kernel_3x3(i, j, data)
        if k[1][1] == "A":
            for p in PATTERNS:
                if k[0][0] == p[0] and k[0][2] == p[1] and k[2][0] == p[2] and k[2][2] == p[3]:
                    count += 1
                    
print(count)