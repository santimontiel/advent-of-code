from dataclasses import dataclass
from typing import List
from utils import summary

def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()
    

@dataclass
class Position:
    x: int
    y: int


@summary
def part_1(data: str, mult: int = 1) -> int:

    def manhattan(p1: Position, p2: Position) -> int:
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
    
    # Get the positions of all galaxies.
    galaxies = [Position(r, c) for r, line in enumerate(data)
                for c, char in enumerate(line) if char == "#"]
    
    # Get the rows and columns to expand.
    rows_to_expand = [r for r, row in enumerate(data) if not "#" in row]
    cols_to_expand = [c for c, _ in enumerate(data[0])
                      if not "#" in [row[c] for row in data]]

    # Expand the galaxies.
    mult = (mult - 1) if mult > 1 else 1
    for galaxy in galaxies:
        galaxy.x += mult * sum(list(map(lambda x: x < galaxy.x, rows_to_expand)))
        galaxy.y += mult * sum(list(map(lambda x: x < galaxy.y, cols_to_expand)))

    # Calculate Manhattan distance (minimum) for all pairs of galaxies.
    distances = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distances.append(manhattan(galaxies[i], galaxies[j]))    

    return sum(distances)


@summary
def part_2(data: str) -> int:
    return part_1(data, mult=1_000_000)


def main() -> None:
    data = read_input("../inputs/day_11.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()