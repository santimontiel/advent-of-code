""" Advent of Code 2021. Day 2: Dive!
__author__: Santiago Montiel Marín
"""

import doctest
from typing import List

def parse_text(raw_puzzle: str) -> List[int]:
    with open(raw_puzzle) as f:
        text = f.readlines()
        clean_puzzle = []
        for line in text:
            (k, v) = line.split(' ')
            v = int(v)
            clean_puzzle.append((k,v))
    return clean_puzzle

def part1(puzzle: List[str]) -> int:
    """
    Args:
    
    Return:

    Test:
        >>> part1([('forward', 5), ('down', 5), ('forward', 8), \
            ('up', 3), ('down', 8), ('forward', 2)])
        150
    """
    hor, ver = 0, 0
    for k,v in puzzle:
        if k == "forward":  hor += v
        elif k == "down":   ver += v
        elif k == "up":     ver -= v
    return hor*ver

def part2(puzzle: List[str]) -> int:
    """
    Args:
    
    Return:
    
    Test:
        >>> part2([('forward', 5), ('down', 5), ('forward', 8), \
            ('up', 3), ('down', 8), ('forward', 2)])
        900
    """
    hor, ver, aim = 0, 0, 0
    for k,v in puzzle:
        if k == "forward":  hor, ver = hor+v, ver+aim*v
        elif k == "down":   aim += v
        elif k == "up":     aim -= v
    return hor*ver

def main(args=None):
    doctest.testmod(verbose=True)
    puzzle = parse_text("input02.txt")
    print(f"Answer to question 1 is: {part1(puzzle)}")
    print(f"Answer to question 2 is: {part2(puzzle)}")

if __name__ == "__main__":
    main()