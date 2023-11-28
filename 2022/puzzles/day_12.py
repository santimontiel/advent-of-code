"""
"""
from typing import List, Tuple
import time

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"Elapsed time for {f.__name__}: {((te-ts) * 1e3):.3f} ms")
        return result

    return timed

# Parse the input data.
def read_input(path: str) -> List[str]:
    with open(path, "r") as fin:
        return [line.strip() for line in fin.readlines()]
    

# Neighbor query function.
def get_neighbours(data, pos) -> List[Tuple[int, int]]:

    x, y = pos[0], pos[1]
    h, w = len(data), len(data[0])
    neighbours = []
    if y > 0:
        neighbours.append((x, y-1))
    if y < w-1:
        neighbours.append((x, y+1))
    if x > 0:
        neighbours.append((x-1, y))
    if x < h-1:
        neighbours.append((x+1, y))
    return neighbours


def validate_neighbours(data, pos, neighbours) -> List[Tuple[int, int]]:

    curr_value = data[pos[0]][pos[1]]
    valid_neighbours = []
    for neighbour in neighbours:
        # print(f"Neighbour: {neighbour}")
        next_value = data[neighbour[0]][neighbour[1]]
        if ord(next_value) - ord(curr_value) <= 1:
            valid_neighbours.append(neighbour)

    return valid_neighbours

# Breadth-first search.
def bfs(data, start, end) -> int:

    visited = set()
    queue = [(0, start)]

    while len(queue) > 0:
        curr = queue.pop(0)
        # print(f"Currently visiting: {curr[1]}")
        if curr[1] == end:
            return curr[0]
        if curr[1] not in visited:
            visited.add(curr[1])
            neighbours = get_neighbours(data, curr[1])
            # print(f"Number of neighbours: {len(neighbours)}")
            valid_neighbours = validate_neighbours(data, curr[1], neighbours)
            for n in valid_neighbours:
                queue.append((curr[0] + 1, n))
                
    return 99999

# Part 1.
@timeit
def part_1(data: List[str]) -> int:
    
    # Get the start and end position.
    start, end = None, None
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
        if start and end:
            break
    data[start[0]] = data[start[0]].replace("S", "a")
    data[end[0]] = data[end[0]].replace("E", "z")
    # print(f"Starting position: {start}. Ending position: {end}.")

    # Perform BFS.
    return bfs(data, start, end)    

@timeit
def part_2(data: List[str]) -> int:

    # Get the start and end position.
    start, end = None, None
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)
        if start and end:
            break
    data[start[0]] = data[start[0]].replace("S", "a")
    data[end[0]] = data[end[0]].replace("E", "z")

    # Do this for all 'a' cells.
    distances = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if data[i][j] == "a":
                distances.append(bfs(data, (i, j), end))

    return min(distances)

test_input=[
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

print(part_1(test_input))
print(part_1(read_input("../data/day_12.txt")))
print(part_2(read_input("../data/day_12.txt")))

# print(read_input("../data/day_12.txt"))