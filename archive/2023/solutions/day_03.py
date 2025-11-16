from typing import List, Tuple
from utils import summary


def read_input(file_path: str) -> List[int]:
    with open(file_path, "r") as fin:
        return [line.strip() for line in fin.readlines()]
    

def get_part_numbers(data: List[str]) -> List[Tuple[int, int, int, int]]:
    numbers = []
    for i, line in enumerate(data):

        current_number = ""
        for j, char in enumerate(line):
            
            if char.isnumeric():
                current_number += char
            else:
                try:
                    numbers.append((int(current_number), i, j-len(current_number),  j-1))
                except ValueError:
                    pass
                current_number = ""

            if j == len(line) - 1:
                try:
                    numbers.append((int(current_number), i, j-len(current_number)+1, j))
                except ValueError:
                    pass
            
    return numbers


def get_gears(data: List[str]) -> List[Tuple[int, int]]:

    gears = []
    
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c == "*":
                gears.append((i, j))
    
    return gears


def get_neighbours(
        part_number: Tuple[int, ...], h: int, w: int
    ) -> List[Tuple[int, int]]:

    n, r, sc, ec = part_number
    neighbours = []

    # Upper row.
    if r > 0:
        for i in range(sc, ec + 1):
            neighbours.append((r-1, i))

    # Lower row.
    if r < h-1:
        for i in range(sc, ec + 1):
            neighbours.append((r+1, i))

    # Left neighbour.
    if sc > 0:
        neighbours.append((r, sc-1))

    # Right neighbour.
    if ec < w-1:
        neighbours.append((r, ec+1))

    # Left-up neighbour.
    if r > 0 and sc > 0:
        neighbours.append((r-1, sc-1))

    # Left-down neighbour.
    if r < h-1 and sc > 0:
        neighbours.append((r+1, sc-1))

    # Right-up neighbour.
    if r > 0 and ec < w-1:
        neighbours.append((r-1, ec+1))

    # Right-down neighbour.
    if r < h-1 and ec < w-1:
        neighbours.append((r+1, ec+1))

    return list(set(neighbours))


def get_gears_neighbours(pos, part_numbers):
    x, y = pos[0], pos[1]
    q = list(filter(lambda a: x-1 <= a[1] <= x+1 and y in list(range(a[2]-1, a[3]+2)), part_numbers))
    return q


def is_adjacent(data: List[str], neighbours: List[Tuple[int, int]]) -> bool:
    for neighbour in neighbours:
        i, j = neighbour
        if data[i][j] != "." and not data[i][j].isnumeric():
            return True
    return False


@summary
def part_1(data: List[str]) -> int:

    counter = 0
    part_numbers = get_part_numbers(data)
    h, w = len(data), len(data[0])

    for number in part_numbers:
        neighbours = get_neighbours(number, h, w)
        if is_adjacent(data, neighbours):
            counter += number[0]
    return counter


@summary
def part_2(data: List[str]) -> int:

    part_numbers = get_part_numbers(data)
    gears = get_gears(data)

    counter = 0
    for gear in gears:
        neighbours = get_gears_neighbours(gear, part_numbers)
        if len(neighbours) == 2:
            counter += neighbours[0][0] * neighbours[1][0]

    return counter


def main():

    data = read_input("../inputs/day_03.txt")
    res_1 = part_1(data)
    res_2 = part_2(data)


if __name__ == "__main__":
    main()