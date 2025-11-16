"""Advent of Code 2021. Day 5: Hydrothermal Venture.
__author__: Santiago Montiel Marín
"""
from typing import List, Tuple

def read_input(file_path: str) -> List[Tuple[int, ...]]:
    with open(file_path, "r") as fin:
        return [tuple(map(int, line.strip().replace(" -> ", ",").split(","))) for line in fin]
    

def part_1(data: List[Tuple[int, ...]]) -> int:

    positions = {}
    for line in data:

        # Parsing the line.
        x1, y1, x2, y2 = line

        # Dealing with horizontal lines.
        if x1 == x2:
            if y1 <= y2:
                iterator = range(y1, y2+1, 1)
            elif y1 > y2:
                iterator = range(y1, y2-1, -1)

            for y in iterator:
                if (x1, y) in positions.keys():
                    positions[(x1, y)] += 1
                else:
                    positions[(x1, y)] = 1

        # Dealing with vertical lines.
        if y1 == y2:

            if x1 <= x2:
                iterator = range(x1, x2+1, 1)
            elif x1 > x2:
                iterator = range(x1, x2-1, -1)

            for x in iterator:
                if (x, y1) in positions.keys():
                    positions[(x, y1)] += 1
                else:
                    positions[(x, y1)] = 1

    cnt = len(list(filter(lambda x: x >= 2, positions.values())))

    return cnt


def part_2(data: List[Tuple[int, ...]]) -> int:

    positions = {}
    for line in data:

        # Parsing the line.
        x1, y1, x2, y2 = line

        # Dealing with horizontal lines.
        if x1 == x2:
            if y1 <= y2:
                iterator = range(y1, y2+1, 1)
            elif y1 > y2:
                iterator = range(y1, y2-1, -1)

            for y in iterator:
                if (x1, y) in positions.keys():
                    positions[(x1, y)] += 1
                else:
                    positions[(x1, y)] = 1

        # Dealing with vertical lines.
        elif y1 == y2:

            if x1 <= x2:
                iterator = range(x1, x2+1, 1)
            elif x1 > x2:
                iterator = range(x1, x2-1, -1)

            for x in iterator:
                if (x, y1) in positions.keys():
                    positions[(x, y1)] += 1
                else:
                    positions[(x, y1)] = 1

        # Dealing with diagonal lines.
        else:
            
            if x1 <= x2:
                itx = range(x1, x2 + 1, 1)
            else:
                itx = range(x1, x2 - 1, -1)
            
            if y1 <= y2:
                ity = range(y1, y2 + 1, 1)
            else:
                ity = range(y1, y2 - 1, -1)

            for x, y in zip(itx, ity):
                if (x, y) in positions.keys():
                    positions[(x, y)] += 1
                else:
                    positions[(x, y)] = 1

    cnt = len(list(filter(lambda x: x >= 2, positions.values())))
    return cnt


# print(read_input("../data/input05.txt"))
print(part_1(read_input("../data/input05.txt")))
print(part_2(read_input("../data/input05.txt")))