""" Advent of Code 2021. Day X:
__author__: Santiago Montiel Marín
"""

from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            clean_puzzle.append(int(line))
    return clean_puzzle

def part1(puzzle: List[int]) -> int:
    pass

def part2(puzzle: List[int]) -> int:
    pass

def main(args=None):
    puzzle = parse_text("input01.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()